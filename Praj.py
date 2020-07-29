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

