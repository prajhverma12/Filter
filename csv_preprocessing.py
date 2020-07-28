
import numpy as np
import pandas as pd
import csv
dataset = pd.read_csv("CF-Insider-Trading-equities-28-04-2020-to-28-07-2020.csv")
X = dataset.iloc[:, :].values
groups = ['Promoters', 'Promoter Group']
dataset = dataset[dataset['category of person'].isin(groups)]

