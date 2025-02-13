import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class TTFNN:
    def __init__(self, created_training_data, created_testing_data):
        self.normalized_training_data = self._normalize(created_training_data)
        self.testing_data = created_testing_data
        self.model = None

    def train_existing_TTFNN(self):
        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(self.normalized_training_data, self.testing_data, test_size=0.2, random_state=42)
        
        print("Create NN w/ : relu activation 3 layers, 8 nodes")
        # Create a neural network model with additional layers
        model = Sequential([
            Dense(8, input_shape=(X_train.shape[1],), activation='relu'),
            Dense(8, activation='relu'),  # Existing hidden layer
            Dense(8, activation='relu'),  # New hidden layer
            Dense(3, activation='softmax')  # Assuming 3 classes for classification
        ])

        print("Compile w/ adam optimizer, categorical cross entropy loss function")
        # Compile the model
        # types: binarycross_entropy, categorical_crossentropy
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

        print("Train w/ 50 epochs, batch size 4, and 0.2 validation split")
        # Train the model
        model.fit(X_train, y_train, epochs=50, batch_size=4, validation_split=0.2)

        # Evaluate the model on the test set
        loss, accuracy = model.evaluate(X_test, y_test)
        print(f"Test Accuracy: {accuracy:.4f}")

    def _normalize(self, training_data):
        # Normalize the data
        scaler = StandardScaler()
        return scaler.fit_transform(training_data)


