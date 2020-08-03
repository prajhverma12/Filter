import pandas as pd
import dateutility as date
import time
import subprocess
import os
import fileutility as file

def download_csv():
    cmd = "start chrome \"https://www.nseindia.com/api/corporates-pit?index=equities&from_date="+ date.beforeDate() + "&to_date=" + date.dateToday() + "&csv=true\""
    returned_value = subprocess.call(cmd, shell=True)
    print("Return value for Main Sheet : {}".format(returned_value))
    time.sleep(10)
      
def filterStocks(filename):
    try:
        dataset = pd.read_csv(filename)
    except:
        print("File not present {}, Downloading...".format(filename))
        download_csv()
        if file.checkfile(filename):
            consolidatedData = filterStocks(filename)
            return consolidatedData
        else:
            logging.error("File {} not downloaded, Please check net connection and try again...".format(filename))        
    
    else:
        for header in dataset.columns:
            dataset = dataset.rename(columns={header: header.strip()})
        
        print("Formatted Header")
        
        personGroup = ['Promoters', 'Promoter Group']
        dataset = dataset[dataset['CATEGORY OF PERSON'].isin(personGroup)]
        
        print('Filtered "CATEGORY OF PERSON" row')
        
        aquisitionGroup = ['Market Purchase']
        dataset = dataset[dataset['MODE OF ACQUISITION'].isin(aquisitionGroup)]
        
        print('Filtered "MODE OF ACQUISITION" row')
        
        filteredData = dataset
        
        headerList = list(filteredData.columns)
            
        headerList.remove("VALUE OF SECURITY (ACQUIRED/DISPLOSED)")
        headerList.remove("SYMBOL")
        
        filteredData = filteredData.drop(headerList, axis=1)
        
        print("Removed unnecessary rows")
        
        consolidatedData = filteredData
        
        consolidatedData["VALUE OF SECURITY (ACQUIRED/DISPLOSED)"] = consolidatedData["VALUE OF SECURITY (ACQUIRED/DISPLOSED)"].astype(str).astype(float)
        consolidatedData = consolidatedData.groupby('SYMBOL',as_index=False)['VALUE OF SECURITY (ACQUIRED/DISPLOSED)'].sum()
        
        print("Consolidated Data")
        
        consolidatedData.drop(consolidatedData[consolidatedData['VALUE OF SECURITY (ACQUIRED/DISPLOSED)'] < 10000000].index, inplace = True)
        
        print("Removed values less than 1Cr")
        
        consolidatedData.sort_values(by=['VALUE OF SECURITY (ACQUIRED/DISPLOSED)'], inplace=True, ascending=False)
        
        print("Sorted the remaining Data in descending format")
        
        if not file.checkfile("Stocks-" + date.dateToday() + ".csv"):
            consolidatedData.to_csv("Stocks-"+ date.dateToday() +".csv", header=True, index=False, sep=',')
            print("File not present {}, Converting Dataset into csv".format("Stocks-" + date.dateToday() + ".csv"))
        else:
            print("File already present {}, Deleting the file".format("Stocks-" + date.dateToday() + ".csv"))
            file.deletefile("Stocks-" + date.dateToday() + ".csv")
            consolidatedData.to_csv("Stocks-"+ date.dateToday() +".csv", header=True, index=False, sep=',')
            
        return consolidatedData

