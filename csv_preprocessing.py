
import numpy as np
import pandas as pd
import csv
dataset = pd.read_csv("CF-Insider-Trading-equities-28-04-2020-to-28-07-2020.csv")

print(type(dataset.head(0)))


new_list = []

for i in dataset.head(0):
    new_list.append(i.strip())

print(new_list)

X = dataset.iloc[:, :].values

#print(X)

groups = ['Promoters', 'Promoter Group']
dataset = dataset[dataset['category of person'].isin(groups)]

#print(dataset['SYMBOL'])::
