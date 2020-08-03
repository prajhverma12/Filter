import os

def checkfile(filename):
    arr = os.listdir('.')
    #print(arr)
    if filename in arr:
        print("File {} present in the directory".format(filename))
        return True
    else:
        print("File {} not present in the directory".format(filename))
        return False
    
def deletefile(filename):
    if checkfile(filename):
        os.remove(filename)
    else:
        print("File {} not present in the directory".format(filename))