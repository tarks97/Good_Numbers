from driver_load import driver_load
from time import sleep
from file_manipulation import Reader
from selenium.webdriver.common.keys import Keys



def telmoreSearch(url):
    print("Telmore")

    driver = driver_load()
    sleep(1)
    driver.get(url)
    try:

        buttonCustomer = driver.find_element_by_xpath(
            """//*[@id="menu"]/div/ul/li[1]/a""")
        buttonCustomer.click()
        sleep(2)
        
        buttonCustomer = driver.find_element_by_xpath(
            """//*[@id="content"]/div[1]/div/div/div[2]/div[3]/div[2]/div/div/div[2]/div[4]/span/a""") 
        buttonCustomer.click()
        sleep(3)

        buttonCustomer = driver.find_element_by_xpath(
            """//*[@id="step-1"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/a""")
        buttonCustomer.click()
        sleep(3)

          
      
          # div Sa Label Tagovima U Kojima Se Nalaze Brojevi niz u pitanju
        
        
        with open("brojevi.txt", "+a",) as fajl:
           brojevi = Reader("Dobribrojevi.txt")
           for broj in brojevi:

                search=driver.find_element_by_xpath("""//*[@id="formly_6_custom-input-group-search_numberSearch_0"]""")
                search.send_keys(broj[:8])

                
                buttonCustomer = driver.find_element_by_xpath("""/html/body/div[1]/div[2]/div/div[2]/div/div/div/div/div[2]/section[1]/div/div/div[2]/div[2]/div/div/div/div[4]/form/ng-form/div[1]/ng-form/div[1]/div/span[3]/button""")
                buttonCustomer.click()
                sleep(3)

                search.send_keys(Keys.CONTROL + "a")
                search.send_keys(Keys.DELETE)

                if not driver.find_element_by_xpath("""//*[@id="no-numbers"]"""):
                    fajl.write("Telmore %s \n ", broj)
                
        fajl.close()
    except Exception as e: 
        print(e)
    driver.close()

URLS = Reader("urls.txt")
for url in URLS:
    if "telmore" in str(url):
        telmoreSearch(url)