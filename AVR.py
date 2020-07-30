# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 06:22:20 2020

@author: Arnav Verma
"""

def checkfile(filename):
    import os
    arr = os.listdir('.')
    print(arr)
    if filename in arr:
        return True
    else:
        return False
    
if checkfile("CF-Insider-Trading-equities-30-04-2020-to-30-07-2020.csv"):
    print("true")

else:
    print("false")    