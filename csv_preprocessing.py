import pandas as pd
import dateutility as date
import time
import subprocess
import os
import fileutility as file
import logging

def download_csv():
    cmd = "start chrome \"https://www.nseindia.com/api/corporates-pit?index=equities&from_date="+ date.beforeDate() + "&to_date=" + date.dateToday() + "&csv=true\""
    returned_value = subprocess.call(cmd, shell=True)
    print("Return value for Main Sheet : {}".format(returned_value))
    time.sleep(10)
      
def filterStocks(filename):
    try:
        dataset = pd.read_csv(filename)
    except:
        download_csv()
        if file.checkfile(filename):
            consolidatedData = filterStocks(filename)
            return consolidatedData
        else:
            print("File {} not downloaded, Please check net connection and try again...".format(filename))        
    
    else:
        for header in dataset.columns:
            dataset = dataset.rename(columns={header: header.strip()})
        
        personGroup = ['Promoters', 'Promoter Group']
        dataset = dataset[dataset['CATEGORY OF PERSON'].isin(personGroup)]
        
        aquisitionGroup = ['Market Purchase']
        dataset = dataset[dataset['MODE OF ACQUISITION'].isin(aquisitionGroup)]
        
        filteredData = dataset
        
        headerList = list(filteredData.columns)
            
        headerList.remove("VALUE OF SECURITY (ACQUIRED/DISPLOSED)")
        headerList.remove("SYMBOL")
        
        filteredData = filteredData.drop(headerList, axis=1)
        
        consolidatedData = filteredData
        
        consolidatedData["VALUE OF SECURITY (ACQUIRED/DISPLOSED)"] = consolidatedData["VALUE OF SECURITY (ACQUIRED/DISPLOSED)"].astype(str).astype(float)
        consolidatedData = consolidatedData.groupby('SYMBOL',as_index=False)['VALUE OF SECURITY (ACQUIRED/DISPLOSED)'].sum()
        
        
        consolidatedData.drop(consolidatedData[consolidatedData['VALUE OF SECURITY (ACQUIRED/DISPLOSED)'] < 10000000].index, inplace = True)
        
        consolidatedData.sort_values(by=['VALUE OF SECURITY (ACQUIRED/DISPLOSED)'], inplace=True, ascending=False)
    
        if not file.checkfile("Stocks-" + date.dateToday() + ".csv"):
            consolidatedData.to_csv("Stocks-"+ date.dateToday() +".csv", header=True, index=False, sep=',')
        else:
            file.deletefile("Stocks-" + date.dateToday() + ".csv")
            consolidatedData.to_csv("Stocks-"+ date.dateToday() +".csv", header=True, index=False, sep=',')
            
        return consolidatedData

