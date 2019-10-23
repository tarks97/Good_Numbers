import os
import csv

def Reader(nameOfAFile):
    statment = os.path.exists(nameOfAFile)
    print(os.getcwd())
    if(statment == True):
        skup = []
        with open(nameOfAFile, "r") as fajl:
            for line in fajl:
                skup.append(line)
        return skup
    else:
        print("file doesnt exist")
        return None
    return