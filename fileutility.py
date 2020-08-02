import os
import logging

def checkfile(filename):
    arr = os.listdir('.')
    #print(arr)
    if filename in arr:
        logging.info("File {} present in the directory".format(filename))
        return True
    else:
        logging.info("File {} not present in the directory".format(filename))
        return False
    
def deletefile(filename):
    if checkfile(filename):
        os.remove(filename)
    else:
        logging.info("File {} not present in the directory".format(filename))