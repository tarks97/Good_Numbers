import urllib.request
import json
from algoritmi import *


def getOister():
    with urllib.request.urlopen("https://www.oister.dk/api/checkout/available-numbers?variantCode=2_HOUR_2_GB_49&pattern=&fbclid=IwAR0jkLau-N3jZL6NpSMHklg1Rg5RftqegWj8uY6YQ_Tf2m2VWVftVuBH7FA") as url:
        oisterDk = json.loads(url.read().decode())
        numbers = set()  # Skup(nema duplikata)
        availableNumbers = oisterDk['availableNumbers']
        with open("brojevi.txt", "+a",) as fajl:
            for phoneNum in availableNumbers:
                numberText = phoneNum
                try:
                    intNumber = int(numberText)
                except:
                    continue
                numbers.add(numberText)
                #radi                                                                                                                                                                         #ova radi xx0000
                print(phoneNum)
                if xxxyyyincreasingone(intNumber) == True or nnx0x0(intNumber) == True or xyxynO(intNumber) == True or xOxOxO(intNumber) == True or nOnOnO(intNumber) == True or xxxxxx(intNumber) == True or increasing1reducing(intNumber) == True or increasing5reducing(intNumber) == True or xxxyyy(intNumber) == True or xysxys(intNumber) == True or xxOOOO(intNumber) == True or xyxyxy(intNumber) == True or ssxyxyxs(intNumber) == True or xyxyss(intNumber) == True:

                    fajl.write("OISTER: %s \n" % numberText)
                    print("GOOOOOOOD NUMBER")
                else:
                    print("not good number")


