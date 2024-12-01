import os
import sys

data = ""

def getData(fileName):
    strPath = os.path.join(sys.path[0], fileName)
    with open(strPath) as fileObject:
        data = fileObject.read().split('\n')

    return data