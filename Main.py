import csv_preprocessing as cp
import subprocess
import dateutility as date
import time
import stockprocessing as sp



def download_csv():
    cmd = "start chrome \"https://www.nseindia.com/api/corporates-pit?index=equities&from_date="+ date.beforeDate() + "&to_date=" + date.dateToday() + "&csv=true\""
    returned_value = subprocess.call(cmd, shell=True)
    print("Return value for Main Sheet : {}".format(returned_value))
    time.sleep(10)
    
def download_stock_csv(stock):
    cmd = "start chrome \"https://www.nseindia.com/api/corporates-pit?index=equities&symbol=" + stock + "&csv=true\""
    returned_value = subprocess.call(cmd, shell=True)
    print("Returned value for {} : {}".format(stock, returned_value))
    time.sleep(1)

def getStockCSV():
    fileName = "CF-Insider-Trading-equities-" + date.beforeDate() + "-to-" + date.dateToday() +".csv"
    print(fileName)
    stocks = cp.filterStocks(fileName)
    stockList = stocks.iloc[:, 0].values.tolist()
    #print(stockList)

    for stock in stockList:
        print(stock)
        download_stock_csv(stock)
    return stockList


#download_csv()

    

