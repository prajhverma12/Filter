# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 06:22:20 2020

@author: Arnav Verma
"""

import pandas as pd

dataset = pd.read_csv("CF-Insider-Trading-equities-ALEMBICLTD-30-Jul-2020.csv")

for header in dataset.columns:
    dataset = dataset.rename(columns={header: header.strip()})

personGroup = ['Promoters', 'Promoter Group']
dataset = dataset[dataset['CATEGORY OF PERSON'].isin(personGroup)]
    
aquisitionGroup = ['Market Purchase']
dataset = dataset[dataset['MODE OF ACQUISITION'].isin(aquisitionGroup)]

filteredData = dataset

headerlist = list(filteredData.columns)
headerlist.remove("VALUE OF SECURITY (ACQUIRED/DISPLOSED)")
headerlist.remove("SYMBOL")
headerlist.remove("NO. OF SECURITIES (ACQUIRED/DISPLOSED)")

filteredData = filteredData.drop(headerlist, axis=1)
ValueOfSecurity = filteredData.iloc[:,-1].values.tolist()
NoOfSecurity = filteredData.iloc[:,-2].values.tolist()
Valuesum = sum(ValueOfSecurity)
Nosum = sum(NoOfSecurity)
buyprice = Valuesum/Nosum