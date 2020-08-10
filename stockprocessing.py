import pandas as pd

def getBuyPrice(filename):
    dataset = pd.read_csv("Downloads/" + filename)
    
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
    
    if len(NoOfSecurity) == 0:
        buyprice = 0
    else:    
        Valuesum = sum(ValueOfSecurity)
        Nosum = sum(NoOfSecurity)
        buyprice = Valuesum/Nosum
    
    return buyprice