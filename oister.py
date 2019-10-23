from driver_load import driver_load
from time import sleep
from algoritmi import *

def oister(url):
    print("OISTER")

    driver = driver_load()
    sleep(1)
    driver.get(url)
    try:

        buttonCustomer = driver.find_element_by_xpath(
            """//*[@id="navigation"]/div/div[1]/div[2]/div/div/ul/li[2]/a""")
        buttonCustomer.click()
        sleep(2)
        
        buttonCustomer = driver.find_element_by_xpath(
            """//*[@id="navigation"]/div/div[1]/div[2]/div/div/ul/li[2]/div[2]/ul/li[1]/a""") 
        buttonCustomer.click()
        sleep(3)

        buttonCustomer = driver.find_element_by_xpath(
            """/html/body/main/div/div[1]/section/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/button""")
        buttonCustomer.click()
        sleep(3)

        try:
            # cookiesButton = driver.find_element_by_xpath("""/html/body/div[10]/div[2]/div[4]/div[2]/div/a""").click()
            driver.execute_script("window.scrollTo(0, 400)") 
        except:
            pass
        buttonCustomer = driver.find_element_by_xpath(
            """/html/body/main/div/div/div/div[3]/div[2]/div/div""").click()
        sleep(3)

        try:
            # cookiesButton = driver.find_element_by_xpath("""/html/body/div[10]/div[2]/div[4]/div[2]/div/a""").click()
            driver.execute_script("window.scrollTo(0, 400)") 
        except:
            pass
        buttonCustomer = driver.find_element_by_xpath(
            """//*[@id="card__-1"]/div/div[3]/div/div/div/div/form/div[1]/div[2]/div""").click()
        sleep(3)
        

        number_labels = driver.find_element_by_xpath("""/html/body/main/div/div/div[2]/div[2]/div/div/div/div/div[3]/div/div/div/div/form/div[4]/div[2]/ul/li[1]/div""").find_elements_by_tag_name(
            "span")  # div Sa Label Tagovima U Kojima Se Nalaze Brojevi niz u pitanju
        
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
                    
                    fajl.write("OISTER: %s \n" % numberText)
                    print("GOOOOOOOD NUMBER")
                else:               
                    print("not good number")
            
            fajl.close()
    except: 
        pass
    driver.close()