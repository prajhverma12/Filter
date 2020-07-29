import csv_preprocessing as cp
import subprocess

def getStockCSV():
    stocks = cp.filterStocks("CF-Insider-Trading-equities-29-04-2020-to-29-07-2020.csv")
    stockList = stocks.iloc[:, 0].values.tolist()

    for stock in stockList:
        cmd = "start chrome \"https://www.nseindia.com/api/corporates-pit?index=equities&symbol=" + i + "&csv=true\""
        #returned_value = subprocess.call(cmd, shell=True)
        #print("Returned value for {} : {}".format(i, returned_value))



#getStockCSV()