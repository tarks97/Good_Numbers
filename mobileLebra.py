from driver_load import driver_load
from time import sleep
from algoritmi import *

def mobileLebara(url):
    print("MOBILELEBARA")

    driver = driver_load()
    sleep(1)
    driver.get(url)

    try:
        buttonCustomer = driver.find_element_by_xpath(
            """/html/body/main/header/div/div/div/div/div[1]/ul/li[4]/a""")
        buttonCustomer.click()
        sleep(2)
        number_labels = driver.find_element_by_xpath("""/html/body/main/div[6]/div/div[3]/div/div/div/div[2]""").find_elements_by_tag_name(
            "input")  # div Sa Label Tagovima U Kojima Se Nalaze Brojevi niz u pitanju
        
        numbers = set()  # Skup(nema duplikata)
        intNumber = 0
        with open("brojevi.txt", "+a",) as fajl:
            for number in number_labels:
                numberText = number.get_attribute("value")
                try:
                    intNumber = int(numberText)

                except:
                    continue
                numbers.add(numberText)
                print(numberText)
                                                                                                    #radi                                                                                                                                                                         #ova radi xx0000                             
                if xxxyyyincreasingone(intNumber) == True or nnx0x0(intNumber)==True  or xyxynO(intNumber)==True  or xOxOxO(intNumber)== True  or nOnOnO(intNumber) == True  or xxxxxx(intNumber)==True or increasing1reducing(intNumber)==True or increasing5reducing(intNumber)==True  or xxxyyy(intNumber)==True or xysxys(intNumber)==True or xxOOOO(intNumber)==True or xyxyxy(intNumber)==True or ssxyxyxs(intNumber)==True or xyxyss(intNumber)==True:
                    
                    fajl.write("MOBILELEBARA %s \n" % numberText)
                    print("GOOOOOD NUMBER")
                else:               
                    print("not good number")
                
            fajl.close()
    except:
        pass
    driver.close()