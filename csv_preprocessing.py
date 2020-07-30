import numpy as np
import pandas as pd
import csv
import dateutility as date

def filterStocks(filename):
    try:
        dataset = pd.read_csv(filename)
    except:
        print("file not found")
    
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
    
        consolidatedData.to_csv("Stocks-"+ date.dateToday() +".csv", header=True, index=False, sep=',')
            
        return consolidatedData

x = filterStocks("CF-Insider-Trading-equities-30-04-2020-to-30-07-2020.csv")