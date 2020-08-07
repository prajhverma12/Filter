import csv_preprocessing as cp
import subprocess
import dateutility as date
import time
import stockprocessing as sp
import pandas as pd
import fileutility as file
    
def ConvertToCsv(dictionary):
    df = pd.DataFrame(list(dictionary.items()))
    return df
    
def download_stock_csv(stock):
    cmd = "start chrome \"https://www.nseindia.com/api/corporates-pit?index=equities&symbol=" + stock + "&csv=true\""
    returned_value = subprocess.call(cmd, shell=True)
    print("Returned value for {} : {}".format(stock, returned_value))
    time.sleep(5)
    
def getBuyPriceForStock(stock, filename):
    if file.checkfile(filename):
        buyprice = sp.getBuyPrice(filename)
    
    else:
        print("File not found for {}: {}".format(stock, filename))
        download_stock_csv(stock)
        time.sleep(10)
        buyprice = getBuyPriceForStock(stock, filename)
    
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
        if not file.checkfile(filename):
            download_stock_csv(stock)
        buyprice = getBuyPriceForStock(stock, filename)
        buyprices[stock] = buyprice

    deleteStockCSV(stockList)        
    return buyprices

def deleteStockCSV(stocklist):
    for stock in stocklist:
        filename = "CF-Insider-Trading-equities-"+ stock + "-" + date.dateFormatforStock() + ".csv"
        print("Deleting the Stock csv file {}".format(filename))
        file.deletefile(filename)
    

if __name__ == "__main__":
    buyprices = getStockCSV()
    df = ConvertToCsv(buyprices)
    if not file.checkfile("AllStocksBuyPrices-" + date.dateToday() + ".csv"):
        df.to_csv("AllStocksBuyPrices-" + date.dateToday() + ".csv", index=False, sep=",")
    else:
        file.deletefile("Stocks-" + date.dateToday() + ".csv")
        df.to_csv("AllStocksBuyPrices-" + date.dateToday() + ".csv", index=False, sep=",")
        
