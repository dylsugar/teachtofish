import yfinance as yf

def automated_inputter():
    # Specify the stock ticker
    ticker = 'AAPL'  # Apple Inc. as an example

    # Fetch the stock data
    stock = yf.Ticker(ticker)

    # Get the income statement
    income_statement = stock.financials
    #print("Income Statement:")
    #print(income_statement)
    #for x in income_statement.index:
    #    print(x)

    # Get the balance sheet
    #balance_sheet = stock.balance_sheet
    #current_assets = balance_sheet.loc['Total Current Assets']
    #current_liabilities = balance_sheet.loc['Total Current Liabilities']
    #print("\nBalance Sheet:")
    #for x in balance_sheet.index:
    #    print(x)

    # Get the cash flow statement
    cash_flow = stock.cashflow
    print("\nCash Flow Statement:")
    #print(cash_flow)
    for x in cash_flow.index:
        print(x)
automated_inputter()
