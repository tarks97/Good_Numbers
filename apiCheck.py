from file_manipulation import Reader
from driver_load import driver_load
from time import sleep
import urllib.request
import json
def func():
    brojevi = Reader("Dobribrojevi.txt")
    urlPattern = "https://www.oister.dk/api/checkout/available-numbers?variantCode=2_HOUR_2_GB_49&pattern="
    for broj in brojevi:
        urlCrafted = urlPattern + str(broj)
        with urllib.request.urlopen(urlCrafted) as url:
            phoneNumbers = json.loads(url.read().decode())
            with open("brojevi.txt", "+a",) as fajl:
                numberText = str(phoneNumbers['availableNumbers']).strip('[]')
                try:
                    intNumber = int(numberText)
                    fajl.write("%d\n",intNumber)
                except:
                    pass
                    # print(e)
            fajl.close()
                
            
            

func()