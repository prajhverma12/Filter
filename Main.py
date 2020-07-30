import csv_preprocessing as cp
import subprocess
import dateutility as date
import time
import stockprocessing as sp
import pandas as pd
    
def ConvertToCsv(dictionary):
    df = pd.DataFrame(list(dictionary.items()))
    return df
    
def download_stock_csv(stock):
    cmd = "start chrome \"https://www.nseindia.com/api/corporates-pit?index=equities&symbol=" + stock + "&csv=true\""
    returned_value = subprocess.call(cmd, shell=True)
    print("Returned value for {} : {}".format(stock, returned_value))
    time.sleep(2)
    
def getBuyPriceForStock(stock, filename):
    if cp.checkfile(filename):
        buyprice = sp.getBuyPrice(filename)
    
    else:
        print("File not found for {}: {}".format(stock, filename))
        download_stock_csv(stock)
        time.sleep(10)
        buyprice = getBuyPriceForStock(stock)
    
    return buyprice

def getStockCSV():
    buyprices = {}
    fileName = "CF-Insider-Trading-equities-" + date.beforeDate() + "-to-" + date.dateToday() + ".csv"
    print(fileName)
    stocks = cp.filterStocks(fileName)
    stockList = stocks.iloc[:, 0].values.tolist()
    #print(stockList)

    for stock in stockList:
        print(stock)
        filename = "CF-Insider-Trading-equities-"+ stock + "-" + date.dateFormatforStock() + ".csv"
        if not cp.checkfile(filename):
            download_stock_csv(stock)
        buyprice = getBuyPriceForStock(stock, filename)
        buyprices[stock] = buyprice
        
    return buyprices

if __name__ == "__main__":
    buyprices = getStockCSV()
    df = ConvertToCsv(buyprices)
    df.to_csv('AllStocksBuyPrices.csv', index=False, sep=",")
