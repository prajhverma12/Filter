import numpy as np
import pandas as pd
import csv

dataset = pd.read_csv("CF-Insider-Trading-equities-29-04-2020-to-29-07-2020.csv")

for a in dataset.columns:
    dataset = dataset.rename(columns={a: a.strip()})

#dataset_new = dataset.rename(columns={'SYMBOL \r\n': 'SYMBOL'})
old_list = []

for i in dataset.head(0):
    old_list.append(i)

print(dataset.head(0))
print(old_list)


X = dataset.iloc[:, :].values

#print(X)

groups = ['Promoters', 'Promoter Group']
dataset = dataset[dataset['CATEGORY OF PERSON'].isin(groups)]

#print(dataset['SYMBOL'])::