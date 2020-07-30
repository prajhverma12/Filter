from datetime import date
from datetime import datetime, timedelta
from dateutil.relativedelta import *

def dateToday():
    date = datetime.now()
    formattedDate = date.strftime("%d-%m-%Y")
    return formattedDate
    
def beforeDate():
    date = datetime.now()
    date = date + relativedelta(months=-3)
    formattedDate = date.strftime("%d-%m-%Y")
    return formattedDate

def dateFormatforStock():
    date = datetime.now()
    formattedDate = date.strftime("%d-%b-%Y")
    return formattedDate

