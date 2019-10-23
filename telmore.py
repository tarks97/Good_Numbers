from driver_load import driver_load
from time import sleep
from algoritmi import *

def telmore(url):
    print("TELMORE")
    driver = driver_load()
    sleep(1)
    driver.get(url)
    try:
        sleep(2)
        number_labels = driver.find_element_by_xpath("""/html/body/div[1]/div[2]/div/div[2]/div/div/div/div/div[2]/section[1]/div/div/div[2]/div[2]/div/div/div/div[3]/div[1]/div[2]""").find_elements_by_tag_name(
            "div")  # div Sa Label Tagovima U Kojima Se Nalaze Brojevi niz u pitanju
        
        numbers = set()  # Skup(nema duplikata)
        intNumber = 0
        with open("brojevi.txt", "+a",) as fajl:
            for number in number_labels:
                numberText = number.text
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
    except:
        pass
    driver.close()