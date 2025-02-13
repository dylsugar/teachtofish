BALANCE_KEY_INDICATORS = [
    "Treasury Shares Number",
    "Ordinary Shares Number",
    "Share Issued",
    "Net Debt",
    "Total Debt",
    "Tangible Book Value",
    "Invested Capital",
    "Working Capital",
    "Net Tangible Assets",
    "Capital Lease Obligations",
    "Common Stock Equity",
    "Total Capitalization",
    "Total Equity Gross Minority Interest",
    "Stockholders Equity",
    "Gains Losses Not Affecting Retained Earnings",
    "Other Equity Adjustments",
    "Retained Earnings",
    "Capital Stock",
    "Common Stock",
    "Total Liabilities Net Minority Interest",
    "Total Non Current Liabilities Net Minority Interest",
    "Other Non Current Liabilities",
    "Tradeand Other Payables Non Current",
    "Long Term Debt And Capital Lease Obligation",
    "Long Term Capital Lease Obligation",
    "Long Term Debt",
    "Current Liabilities",
    "Other Current Liabilities",
    "Current Deferred Liabilities",
    "Current Deferred Revenue",
    "Current Debt And Capital Lease Obligation",
    "Current Capital Lease Obligation",
    "Current Debt",
    "Other Current Borrowings",
    "Commercial Paper",
    "Payables And Accrued Expenses",
    "Payables",
    "Total Tax Payable",
    "Income Tax Payable",
    "Accounts Payable",
    "Total Assets",
    "Total Non Current Assets",
    "Other Non Current Assets",
    "Non Current Deferred Assets",
    "Non Current Deferred Taxes Assets",
    "Investments And Advances",
    "Other Investments",
    "Investmentin Financial Assets",
    "Available For Sale Securities",
    "Net PPE",
    "Accumulated Depreciation",
    "Gross PPE",
    "Leases",
    "Other Properties",
    "Machinery Furniture Equipment",
    "Land And Improvements",
    "Properties",
    "Current Assets",
    "Other Current Assets",
    "Inventory",
    "Receivables",
    "Other Receivables",
    "Accounts Receivable",
    "Cash Cash Equivalents And Short Term Investments",
    "Other Short Term Investments",
    "Cash And Cash Equivalents",
    "Cash Equivalents",
    "Cash Financial",
]

INCOME_KEY_INDICATORS = [
    "Tax Effect Of Unusual Items",
    "Tax Rate For Calcs",
    "Normalized EBITDA",
    "Net Income From Continuing Operation Net Minority Interest",
    "Reconciled Depreciation",
    "Reconciled Cost Of Revenue",
    "EBITDA",
    "EBIT",
    "Net Interest Income",
    "Interest Expense",
    "Interest Income",
    "Normalized Income",
    "Net Income From Continuing And Discontinued Operation",
    "Total Expenses",
    "Total Operating Income As Reported",
    "Diluted Average Shares",
    "Basic Average Shares",
    "Diluted EPS",
    "Basic EPS",
    "Diluted NI Availto Com Stockholders",
    "Net Income Common Stockholders",
    "Net Income",
    "Net Income Including Noncontrolling Interests",
    "Net Income Continuous Operations",
    "Tax Provision",
    "Pretax Income",
    "Other Income Expense",
    "Other Non Operating Income Expenses",
    "Net Non Operating Interest Income Expense",
    "Interest Expense Non Operating",
    "Interest Income Non Operating",
    "Operating Income",
    "Operating Expense",
    "Research And Development",
    "Selling General And Administration",
    "Gross Profit",
    "Cost Of Revenue",
    "Total Revenue",
    "Operating Revenue"
]

CASHFLOW_KEY_INDICATORS = [
    "Free Cash Flow",
    "Repurchase Of Capital Stock",
    "Repayment Of Debt",
    "Issuance Of Debt",
    "Issuance Of Capital Stock",
    "Capital Expenditure",
    "Interest Paid Supplemental Data",
    "Income Tax Paid Supplemental Data",
    "End Cash Position",
    "Beginning Cash Position",
    "Changes In Cash",
    "Financing Cash Flow",
    "Cash Flow From Continuing Financing Activities",
    "Net Other Financing Charges",
    "Cash Dividends Paid",
    "Common Stock Dividend Paid",
    "Net Common Stock Issuance",
    "Common Stock Payments",
    "Common Stock Issuance",
    "Net Issuance Payments Of Debt",
    "Net Short Term Debt Issuance",
    "Net Long Term Debt Issuance",
    "Long Term Debt Payments",
    "Long Term Debt Issuance",
    "Investing Cash Flow",
    "Cash Flow From Continuing Investing Activities",
    "Net Other Investing Changes",
    "Net Investment Purchase And Sale",
    "Sale Of Investment",
    "Purchase Of Investment",
    "Net Business Purchase And Sale",
    "Purchase Of Business",
    "Net PPE Purchase And Sale",
    "Purchase Of PPE",
    "Operating Cash Flow",
    "Cash Flow From Continuing Operating Activities",
    "Change In Working Capital",
    "Change In Other Working Capital",
    "Change In Other Current Liabilities",
    "Change In Other Current Assets",
    "Change In Payables And Accrued Expense",
    "Change In Payable",
    "Change In Account Payable",
    "Change In Inventory",
    "Change In Receivables",
    "Changes In Account Receivables",
    "Other Non Cash Items",
    "Stock Based Compensation",
    "Deferred Tax",
    "Deferred Income Tax",
    "Depreciation Amortization Depletion",
    "Depreciation And Amortization",
    "Net Income From Continuing Operations",
]

SMALL_CAP_TEST_TICKERS = [
    "ACMR",
    "PUBM",
    "HLIT",
    "GCT",
]

MED_CAP_TEST_TICKERS = [
    "SNX",
    "ONTO",
    "DBX",
    "DOX",
    "MTSI"
]

class StockDictionaryStorage:
    def __init__(self):
        self.stockdict = {}

    def add_liquidity_ratio(self, singleStockData):
        self._storage_update(self, "Liquidity", self._liquidity_ratio_calc(singleStockData))

    def add_debt_to_equity_ratio(self, singleStockData):
        self._storage_update(self, "DebtToEquity", self._debt_to_equity_ratio_calc(singleStockData))

    def add_return_on_equity_ratio(self, singleStockData):
        self._storage_update(self, "ReturnOnEquity", self._return_on_equity_ratio_calc(singleStockData))

    def add_operating_cashflow(self, singleStockData):
        self._storage_update(self, "OperatingCashflow", self._search_key_return_value(singleStockData, "Operating Cash Flow"))
    
    def _storage_update(self, analysis_string, setValue):
        return self.stockdict.setdefault(self.stockticker, {}).update({analysis_string: setValue})
    
    def _liquidity_ratio_calc(stockdata):
        try:
            balance_sheet = stockdata.balance_sheet
            total_assets = float(balance_sheet.loc['Total Current Assets'])
            total_liabilities = float(balance_sheet.loc['Total Current Liabilities'])
            return total_assets/total_liabilities
        except ValueError as e:
            print("Value does not exist")

    def _debt_to_equity_ratio_calc(stockdata):
        try:
            income_statement = stockdata.financials
            total_debt = float(income_statement.loc['Total Equity Gross Minority Interest'])
            total_equity = float(income_statement.loc['Gains Losses Not Affecting Retained Earnings'])
            return total_debt/total_equity
        except ValueError as e:
            print(e)

    def _return_on_equity_ratio_calc(stockdata):
        try:
            cash_flow = stockdata.cashflow
            balance_sheet = stockdata.balance_sheet
            net_income = float(cash_flow.loc['Net Income'])
            shareholder_equity = float(balance_sheet.loc['Stockholders Equity'])
            return net_income/shareholder_equity
        except ValueError as e:
            print(e)

    def _search_key_return_value(searchType, searchKey):
        try:
            return float(searchType.loc[str(searchKey)])
        except ValueError as e:
            print(e)

            






