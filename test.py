from NN.TeachToFishNN import TTFNN
from utility import StockDictionaryStorage, SMALL_CAP_TEST_TICKERS
import yfinance as yf

SDS = StockDictionaryStorage()
for singleTicker in SMALL_CAP_TEST_TICKERS:
    stockdata = yf.Ticker(singleTicker)
    SDS.add_liquidity_ratio(stockdata)
    SDS.add_debt_to_equity_ratio(stockdata)
    SDS.add_return_on_equity_ratio(stockdata)
    SDS.add_operating_cashflow(stockdata)

TTFNN = TTFNN(SDS.stockdict)
TTFNN.train_existing_TTFNN()


