from twelvedata import TDClient
import datetime
import csv

td = TDClient(apikey="3df6cf3457334dbd8ad83f1a3dae3227")
NASDAQ_file = csv.reader(open('publicCompanies/NASDAQ.csv', "r"), delimiter=",")
NYSE_file = csv.reader(open('publicCompanies/NYSE.csv', "r"), delimiter=",")

class StockFinder():
    ticker = None

    def __init__(self, companyName):
        for row in NASDAQ_file:
            if companyName in row[1]:
                self.ticker = row[0]
                break
        
        for row in NYSE_file:
            if companyName in row[1]:
                self.ticker = row[0]
                break
        
    def hasTicker(self):
        if self.ticker is None:
            return False
        else:
            return True

    #startDate='YYYY-MM-DD'
    def getStockPrice(self, startDate):
        normalizedDate = datetime.datetime.strptime(startDate, "%Y-%m-%d")
        endDate = normalizedDate + datetime.timedelta(days=15)
        endDate = endDate.strftime('%Y-%m-%d')
        ts = td.time_series(symbol=self.ticker, interval='1day', start_date=startDate, end_date=endDate)
        stockPrices = ts.as_json()

        ret = []

        for s in stockPrices:
            ret.append([s['datetime'],s['close']])
        
        return ret

