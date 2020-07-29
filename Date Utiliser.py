# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 18:30:47 2020

@author: Arnav Verma
"""
from datetime import date
from datetime import datetime, timedelta
from dateutil.relativedelta import *

date = datetime.now()

d1 = date.strftime("%d/%m/%Y")
date = date + relativedelta(months=-3)
#date = AddMonths(datetime.datetime(2010,8,25),3)
d2 = date.strftime("%d/%m/%Y")
print(d1)
print(d2)