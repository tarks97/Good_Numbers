import urllib.request
import json
from algoritmi import *


def getTelmore():
    with urllib.request.urlopen("https://www.telmore.dk/api/common/anumber/numberbatch?cacheBuster=1571590678953") as url:
        phoneNumbers = json.loads(url.read().decode())
        numbers = set()  # Skup(nema duplikata)
        with open("brojevi.txt", "+a",) as fajl:
            for phoneNumber in phoneNumbers:
                numberText = phoneNumber['phoneNumber']
                try:
                    intNumber = int(numberText)
                except:
                    continue
                numbers.add(numberText)
                print(numberText)
                                                                                                    #radi                                                                                                                                                                         #ova radi xx0000                             
                if xxxyyyincreasingone(intNumber) == True or nnx0x0(intNumber)==True  or xyxynO(intNumber)==True  or xOxOxO(intNumber)== True  or nOnOnO(intNumber) == True  or xxxxxx(intNumber)==True or increasing1reducing(intNumber)==True or increasing5reducing(intNumber)==True  or xxxyyy(intNumber)==True or xysxys(intNumber)==True or xxOOOO(intNumber)==True or xyxyxy(intNumber)==True or ssxyxyxs(intNumber)==True or xyxyss(intNumber)==True:
                    
                    fajl.write("TELMORE %s \n" % numberText)
                    print("GOOOOOD NUMBER")
                else:               
                    print("not good number")
            
            fajl.close()
