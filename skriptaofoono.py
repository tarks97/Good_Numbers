from driver_load import driver_load
from time import sleep



def xxxyyyincreasingone(broj):

    temp = broj % 1000
    broj = int(broj/1000)
    broj = broj % 1000
    if (temp-broj) == 1 or (temp-broj) == -1:
        return True
    return False

def xxxyyy(broj):
    temp = broj%1000
    broj = broj/1000
    broj = broj%1000
    if temp%10==temp/10%10 and temp/10%10==temp/100%10 and broj%10==broj/10%10 and broj/10%10==broj/100%10:
        return True
    return False



def xysxys(broj):
    temp = broj % 1000
    broj = broj / 1000
    broj = broj % 1000
    if temp==broj:
        return True
    return False


def xyxyxy(broj):
    br3 = broj % 100
    broj = broj / 100
    br2 = broj % 100
    broj = broj / 100
    br1 = broj % 100
    broj = broj / 100

    if br1==br2 and br3==br2:
        return True
    return False



def ssxyxyxs(broj):
     br3 = broj % 100
     broj = broj / 100
     br2 = broj % 100
     broj = broj / 100
     br1 = broj % 100
     broj = broj / 100

     if  (br1 == br2) and (br3 % 10 == broj % 10) and (br3 / 10 % 10 == br1 / 10 % 10):
        return True
     return False
  
def xyxyss(broj):
      br3 = broj % 100
      broj = broj / 100
      br2 = broj % 100
      broj = broj / 100
      br1 = broj % 100
      broj = broj / 100
      if br1 == br2 and br3 % 10 == br3 / 10 % 10:
           return True
      return False


def xxOOOO(broj):
    if broj % 10 == 0 and broj / 10 % 10 == 0 and broj / 100 % 10 == 0 and broj / 1000 % 10 == 0:
        return True
    return False


def increasing5reducing(broj):
      br3 = broj % 100
      broj = broj / 100
      br2 = broj % 100
      broj = broj / 100
      br1 = broj % 100
      broj = broj / 100
      if (br3 - br2 == 5 or br3 - br2 == -5) and (br2 - br1 == 5 or br2 - br1 == -5) and br1 % 5 == 0:
          return True
      return False


def increasing1reducing(broj):
      br3 = broj % 100
      broj = broj / 100
      br2 = broj % 100
      broj = broj / 100
      br1 = broj % 100
      broj = broj / 100
      if (br3 - br2 == 1 or br3 - br2 == -1) and (br2 - br1 == 1 or br2 - br1 == -1):
          return True
      return False


def xxxxxx(broj):  
    br1 = broj % 10
    broj = broj / 10
    br2 = broj % 10
    broj = broj / 10
    br3 = broj % 10
    broj = broj / 10
    br4 = broj % 10
    broj = broj / 10
    br5 = broj % 10
    broj = broj / 10
    br6 = broj % 10
    if br1 == br2 and br2 == br3 and br3 == br4 and br4 == br5 and br5 == br6:
        return True
    return False    


def nOnOnO(broj):
    if broj % 10 == 0:
       broj = broj / 100
       if broj % 10 == 0:
          broj = broj / 100
          if broj % 10 == 0:
              return True
    return False





def xOxOxO(broj):
      br3 = broj % 100
      broj = broj / 100
      br2 = broj % 100
      broj = broj / 100
      br1 = broj % 100
      broj = broj / 100
      if br1 == br2 and br2 == br3 and br1 % 10 == 0 and br2 % 10 == 0 and br3 % 10 == 0:
          return True
      return False

def xyxynO(broj):
      br3 = broj % 100
      broj = broj / 100
      br2 = broj % 100
      broj = broj / 100
      br1 = broj % 100
      broj = broj / 100
      if br1 == br2 and (br3 % 10 == 0 or br3 / 10 % 10 == 0):
          return True
      return False
def xyxynOtestt(broj):
      if broj % 10 == 0:
          return True
      return False

def main():
    url = "https://mobile.lebara.com/dk/en/checkout/select-number"
    driver = driver_load()
    sleep(1)
    driver.get(url)
    buttonCustomer = driver.find_element_by_xpath(
        """/html/body/main/header/div/div/div/div/div[1]/ul/li[4]/a""")
          # /html/body/main/header/div/div/div/div/div[1]/ul/li[4]/a
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
           if xxxyyyincreasingone(intNumber) == True  or xyxynO(intNumber)==True or xOxOxO(intNumber)== True or nOnOnO(intNumber) == True or xxxxxx(intNumber)==True or increasing1reducing(intNumber)==True or increasing5reducing(intNumber)==True or xxxyyy(intNumber)==True or xysxys(intNumber)==True or xxOOOO(intNumber)==True or xyxyxy(intNumber)==True or ssxyxyxs(intNumber)==True or xyxyss(intNumber)==True:
               fajl.write("%s " % numberText)
               print("DOBAR BROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOJ")
           else:
               print("it s not good number")
        fajl.close()
       
    driver.close()


if __name__ == "__main__":
    while True:
        main()
        sleep(5)
    
