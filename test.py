import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from keras.models import Model
from keras.layers import Input, Dense, Concatenate

# Assume you have the dataset loaded into a DataFrame
df = pd.read_csv('stocks.csv')


def filter_stocks(df, industry, market_cap_threshold):
    df_filtered = df[(df['industry'] == industry) & (df['market_cap'] > market_cap_threshold)]
    return df_filtered

industry = 'Technology'
market_cap_threshold = 1_000_000_000
df_filtered = filter_stocks(df, industry, market_cap_threshold)

df_filtered.fillna(df_filtered.mean(), inplace=True)


scaler = StandardScaler()
numeric_cols = df_filtered.select_dtypes(include=['float64', 'int64']).columns
df_filtered[numeric_cols] = scaler.fit_transform(df_filtered[numeric_cols])


X = df_filtered.drop(columns=['intrinsic_value'])
y = df_filtered['intrinsic_value']

X = X.values
y = y.values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

def create_sub_network(input_dim):
    input_layer = Input(shape=(input_dim,))
    hidden_layer = Dense(32, activation='relu')(input_layer)
    return input_layer, hidden_layer

# Create sub-networks for balance sheet, cash flow, and income statement
input_bs, hidden_bs = create_sub_network(balance_sheet_dim)
input_cf, hidden_cf = create_sub_network(cash_flow_dim)
input_is, hidden_is = create_sub_network(income_statement_dim)

# Concatenate sub-networks
merged = Concatenate()([hidden_bs, hidden_cf, hidden_is])

# Add additional layers for final decision making
merged_hidden = Dense(64, activation='relu')(merged)
output_layer = Dense(1, activation='linear')(merged_hidden)

# Define the model
model = Model(inputs=[input_bs, input_cf, input_is], outputs=output_layer)
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])


# Prepare inputs for the model
X_train_bs = X_train[:, :balance_sheet_dim]
X_train_cf = X_train[:, balance_sheet_dim:(balance_sheet_dim + cash_flow_dim)]
X_train_is = X_train[:, (balance_sheet_dim + cash_flow_dim):]

X_test_bs = X_test[:, :balance_sheet_dim]
X_test_cf = X_test[:, balance_sheet_dim:(balance_sheet_dim + cash_flow_dim)]
X_test_is = X_test[:, (balance_sheet_dim + cash_flow_dim):]

model.fit([X_train_bs, X_train_cf, X_train_is], y_train, epochs=50, batch_size=32, validation_data=([X_test_bs, X_test_cf, X_test_is], y_test))


predictions = model.predict([X_test_bs, X_test_cf, X_test_is])
df_test = pd.DataFrame({
    'actual': y_test,
    'predicted': predictions.flatten()
})

# Sort by predicted intrinsic value to select the top 3 stocks
top_3_stocks = df_test.sort_values(by='predicted', ascending=False).head(3)
print(top_3_stocks)


