import os

def checkfile(filename):
    arr = os.listdir('.')
    #print(arr)
    if filename in arr:
        return True
    else:
        return False
    
def deletefile(filename):
    if checkfile(filename):
        os.remove(filename)
    else:
        print("File {} is not present in the directory".format(filename))