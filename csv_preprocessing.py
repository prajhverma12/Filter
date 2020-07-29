
import numpy as np
import pandas as pd
import csv
dataset = pd.read_csv("CF-Insider-Trading-equities-28-04-2020-to-28-07-2020.csv")

print(type(dataset.head(0)))


new_list = []
old_list = []

for i in dataset.head(0):
    old_list.append(i)
    new_list.append(i.strip())

print(dataset.head(0))
print(new_list)
print(old_list)
for a, b in zip(old_list, new_list):
    print(a.strip(),b)
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
dataset = dataset[dataset['category of person'].isin(groups)]

#print(dataset['SYMBOL'])::
