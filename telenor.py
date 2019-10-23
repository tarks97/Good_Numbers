from driver_load import driver_load
from time import sleep
from algoritmi import *




def telenor(url):
    print("TELENOR")              #####

    driver = driver_load()
    sleep(1)
    driver.get(url)
    try:
        sleep(7)
        try:
            cookiesButton1 = driver.find_element_by_xpath("""/html/body/div[7]/div/div/div[2]/div/div/button[2]""")
            cookiesButton1.click()
        except Exception as e:
            print(e)
            
        buttonCustomer = driver.find_element_by_xpath(
            """/html/body/div[2]/div[1]/div[1]/header/div/div[2]/div[2]/div[2]/div/a""")
        buttonCustomer.click()
        sleep(2)
        email =driver.find_element_by_xpath("""/html/body/div[5]/div/div[1]/div/div[2]/div/form/div[1]/div/input""")
        email.send_keys("rrkk@outlook.dk")
        sleep(3)
        buttonCustomer = driver.find_element_by_xpath(
            """/html/body/div[5]/div/div[1]/div/div[2]/div/form/button""")
        buttonCustomer.click()
        sleep(2)
        pasword =driver.find_element_by_xpath("""/html/body/main/div[1]/form/div[2]/input[2]""")
        pasword.send_keys("Qikckjlcne1=")
        sleep(2)
        buttonCustomer = driver.find_element_by_xpath(
            """/html/body/main/div[1]/form/div[4]/button[1]""")
        buttonCustomer.click()
        sleep(2)
        

        buttonCustomer = driver.find_element_by_xpath(
            """/html/body/div[2]/div[1]/div[1]/header/div/div[2]/div[2]/div[1]/a""")
        buttonCustomer.click()
        sleep(3)
      
        try:
            # cookiesButton = driver.find_element_by_xpath("""/html/body/div[10]/div[2]/div[4]/div[2]/div/a""").click()
            driver.execute_script("window.scrollTo(0, 400)") 
        except:
            pass
        sleep(3)
        buttonCustomer = driver.find_element_by_xpath(
            """/html/body/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/form/div[2]/div[1]/div/div[1]/button/span[2]""")
        buttonCustomer.click()
        sleep(20)
        # try:

        #     UserId= driver.find_element_by_class_name("input")
        # except Exception as e:
        #     print(e)
        # UserId.send_keys("2307933481")
        
        # UserPassword= driver.find_element_by_xpath("""//*[@id="el3feb7ac1f85a460c"]""")
        # UserPassword.send_keys("3967")
        # buttonCustomer = driver.find_element_by_xpath(
        #     """/html/body/div[3]/div[1]/div[2]/div/div[1]/div[1]/div[3]/button""")
        # buttonCustomer.click()
        # sleep(2)
        buttonCustomer = driver.find_element_by_xpath(
            """/html/body/div[3]/div[1]/div[2]/div/div[1]/div[1]/div[3]/button""")
        buttonCustomer.click()
        sleep(10)

    except:
        pass
        # buttonCustomer = driver.find_element_by_xpath(
        #     """  """)
        # buttonCustomer.click()
        # sleep(2)