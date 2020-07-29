# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 10:36:25 2020

@author: Arnav Verma
"""
import numpy as np
import pandas as pd
import csv

dataset = pd.read_csv("CF-Insider-Trading-equities-29-04-2020-to-29-07-2020.csv")

for a in dataset.columns:
    dataset = dataset.rename(columns={a: a.strip()})
    
X = dataset.iloc[:, :].values

groups = ['Promoters', 'Promoter Group']
dataset = dataset[dataset['CATEGORY OF PERSON'].isin(groups)]

groups1 = ['Market Purchase']
dataset = dataset[dataset['MODE OF ACQUISITION'].isin(groups1)]

data = dataset

old_list = []

for i in data.head(0):
    old_list.append(i.strip())
    


old_list.remove("VALUE OF SECURITY (ACQUIRED/DISPLOSED)")
old_list.remove("SYMBOL")


for i in old_list:
    data = data.drop(i, axis=1)

data_consolidate = data

data_consolidate["VALUE OF SECURITY (ACQUIRED/DISPLOSED)"] = data_consolidate["VALUE OF SECURITY (ACQUIRED/DISPLOSED)"].astype(str).astype(float)
data_consolidate = data_consolidate.groupby('SYMBOL',as_index=False)['VALUE OF SECURITY (ACQUIRED/DISPLOSED)'].sum()


data_consolidate.drop(data_consolidate[data_consolidate['VALUE OF SECURITY (ACQUIRED/DISPLOSED)'] < 10000000].index, inplace = True)

data_consolidate.sort_values(by=['VALUE OF SECURITY (ACQUIRED/DISPLOSED)'], inplace=True, ascending=False)
