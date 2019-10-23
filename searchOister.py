from driver_load import driver_load
from time import sleep
from file_manipulation import Reader
from selenium.webdriver.common.keys import Keys



def oisteri(url):
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
          
      
          # div Sa Label Tagovima U Kojima Se Nalaze Brojevi niz u pitanju
        
        
        with open("brojevi.txt", "+a",) as fajl:
           brojevi = Reader("Dobribrojevi.txt")
           for broj in brojevi:

                search=driver.find_element_by_xpath("""/html/body/main/div/div/div[2]/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/form/div[2]/div[1]/div/div/input""")
                search.send_keys(broj[:8])

                
                buttonCustomer = driver.find_element_by_xpath("""/html/body/main/div/div/div[2]/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/form/div[2]/div[2]/button""")
                buttonCustomer.click()
                sleep(3)

                search.send_keys(Keys.CONTROL + "a")
                search.send_keys(Keys.DELETE)

                if not driver.find_element_by_xpath("""//*[@id="card__-1"]/div/div[3]/div/div/div/div/form/div[4]/div/p"""):
                    fajl.write("%s \n ", broj)
                
        fajl.close()
    except Exception as e: 
        print(e)
    driver.close()

URLS = Reader("urls.txt")
for url in URLS:
    if "oister" in str(url):
        oisteri(url)