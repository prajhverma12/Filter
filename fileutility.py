import os

def checkfile(filename):
    arr = os.listdir('./Downloads')
    #print(arr)
    if filename in arr:
        print("File {} present in the directory".format(filename))
        return True
    else:
        print("File {} not present in the directory".format(filename))
        return False
    
def deletefile(filename):
    qualified_filename = "Downloads/" + filename
    if checkfile(filename):
        os.remove(qualified_filename)
    else:
        print("File {} not present in the directory".format(qualified_filename))