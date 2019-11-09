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
def nOnnnOnO(broj):
    if broj % 10 == 0:
       broj = int(broj / 100)
       if broj % 10 == 0:
          broj = int(broj / 10000)
          if broj % 10 == 0:
              return True
    return False




def xxyyiiss(broj):
    br1 = broj % 10
    broj = int(broj / 10)
    br2 = broj % 10
    broj = int(broj / 10)
    br3 = broj % 10
    broj = int(broj / 10)
    br4 = broj % 10
    broj = int(broj / 10)
    br5 = broj % 10
    broj = int(broj / 10)
    br6 = broj % 10
    broj = int(broj / 10)
    br7 = broj % 10
    broj = int(broj / 10)
    br8 = broj % 10
    if br1 == br2 and br3 == br4 and br5 == br6 and br7 == br8:
        return True
    return False 
    



def increasing2reducing(broj):
      br3 = broj % 100
      broj = int(broj / 100)
      br2 = broj % 100
      broj = int(broj / 100)
      br1 = broj % 100
      broj = int(broj / 100)
      if (br3 - br2 == 2 or br3 - br2 == -2) and (br2 - br1 == 2 or br2 - br1 == -2):
          return True
      return False

def increasingFourreducing(broj):
      br3 = broj % 100
      broj = int(broj / 100)
      br2 = broj % 100
      broj = int(broj / 100)
      br1 = broj % 100
      broj = int(broj / 100)
      if (br3 - br2 == 4 or br3 - br2 == -4) and (br2 - br1 == 4 or br2 - br1 == -4):
          return True
      return False

def increasing10reducing(broj):
      br3 = broj % 100
      broj = int(broj / 100)
      br2 = broj % 100
      broj = int(broj / 100)
      br1 = broj % 100
      broj = int(broj / 100)
      if (br3 - br2 == 10 or br3 - br2 == -10) and (br2 - br1 == 10 or br2 - br1 == -10):
          return True
      return False

def increasing50reducing(broj):
      br3 = broj % 100
      broj = int(broj / 100)
      br2 = broj % 100
      broj = int(broj / 100)
      br1 = broj % 100
      broj = int(broj / 100)
      if (br3 - br2 == 50 or br3 - br2 == -50) and (br2 - br1 == 50 or br2 - br1 == -50):
          return True
      return False

def increasing25reducing(broj):
      br3 = broj % 100
      broj = int(broj / 100)
      br2 = broj % 100
      broj = int(broj / 100)
      br1 = broj % 100
      broj = int(broj / 100)
      if (br3 - br2 == 25 or br3 - br2 == -25) and (br2 - br1 == 25 or br2 - br1 == -25):
          return True
      return False






def nnxxxx(broj):  
    br1 = broj % 10
    broj = int(broj / 10)
    br2 = broj % 10
    broj = int(broj / 10)
    br3 = broj % 10
    broj = int(broj / 10)
    br4 = broj % 10
    if br1 == br2 and br2 == br3 and br3 == br4:
        return True
    return False    


def nnxyxy(broj):

    br3 = broj % 100
    broj = int(broj / 100)
    br2 = broj % 100
    broj = int(broj / 100)

    if br3==br2:
        return True
    return False


def nnoonetwothreefour(broj):  
    br1 = broj % 10
    broj = int(broj / 10)
    br2 = broj % 10
    broj = int(broj / 10)
    br3 = broj % 10
    broj = int(broj / 10)
    br4 = broj % 10
    if br1 == 4 and br2 == 3 and br3 == 2 and br4 == 1:
        return True
    return False    


def nnoOneTwoThreeFourFiveSix(broj):  
    br1 = broj % 10
    broj = int(broj / 10)
    br2 = broj % 10
    broj = int(broj / 10)
    br3 = broj % 10
    broj = int(broj / 10)
    br4 = broj % 10
    broj = int(broj / 10)
    br5 = broj % 10
    broj = int(broj / 10)
    br6 = broj % 10
    if br1 == 6 and br2 == 5 and br3 == 4 and br4 == 3 and br5 == 2 and br6 == 1:
        return True
    return False    


def ThreeZeros(broj):  
    br1 = broj % 10
    broj = int(broj / 10)
    br2 = broj % 10
    broj = int(broj / 10)
    br3 = broj % 10
    broj = int(broj / 10)
    br4 = broj % 10
    broj = int(broj / 10)
    br5 = broj % 10
    broj = int(broj / 10)
    br6 = broj % 10
    broj = int(broj / 10)
    br7 = broj % 10
    broj = int(broj / 10)
    br8 = broj % 10
    brojac = 0
    if br1 == 0:
        brojac = brojac + 1
    if br2 == 0:
        brojac = brojac + 1
    if br3 == 0:
        brojac = brojac + 1
    if br4 == 0:
        brojac = brojac + 1
    if br5 == 0:
        brojac = brojac + 1
    if br6 == 0:
        brojac = brojac + 1
    if br7 == 0:
        brojac = brojac + 1
    if br8 == 0:
        brojac = brojac + 1
    
    if brojac >= 3:
        return True
    return False   
def nnx0x0(broj): #   52 68 50 30
    br4= broj %10
    broj = int(broj/10)
    br3 = broj % 10
    broj = int(broj/10)
    br2 = broj % 10
    broj = int(broj/10)
    br1 = broj % 10
    broj = int(broj/10)


    if br4 == 0 and br2 == 0 and br3 == br1:
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
            if xxxyyyincreasingone(intNumber) == True:
                fajl.write("xxxyyyincreasingone  %s \n" % numberText)
                print("GOOOOOD NUMBER")
                
                
                
            elif ThreeZeros(intNumber) == True: 
                fajl.write("ThreeZeros %s \n" % numberText)
                print("GOOOOOD NUMBER")
                
                
            elif nnoOneTwoThreeFourFiveSix(intNumber) == True:
                fajl.write("nnoOneTwoThreeFourFiveSix %s \n" % numberText)
                print("GOOOOOD NUMBER")
            
            
            elif nnxyxy(intNumber) == True:
                fajl.write("nnxyxy %s \n" % numberText)
                print("GOOOOOD NUMBER")
                
            elif nnoonetwothreefour(intNumber) == True:
                fajl.write("nnoonetwothreefour %s \n" % numberText)
                print("GOOOOOD NUMBER")
                    
            elif nnxxxx(intNumber) == True:
                fajl.write("nnxxxx %s \n" % numberText)
                print("GOOOOOD NUMBER")
                
            elif  increasing25reducing(intNumber) == True:
                fajl.write("increasing25reducing %s \n" % numberText)
                print("GOOOOOD NUMBER")
                
            elif increasing50reducing(intNumber) == True:
                fajl.write("increasing50reducing %s \n" % numberText)
                print("GOOOOOD NUMBER")
                
            elif  increasing10reducing(intNumber) == True:
                fajl.write("increasing10reducing %s \n" % numberText)
                print("GOOOOOD NUMBER")
            elif increasing2reducing(intNumber) == True: 
                fajl.write("increasing2reducing %s \n" % numberText)
                print("GOOOOOD NUMBER")
                
                
            elif increasingFourreducing(intNumber) == True:
                fajl.write("increasingFourreducing %s \n" % numberText)
                print("GOOOOOD NUMBER")
                
            elif nOnnnOnO(intNumber) == True:
                fajl.write("nOnnnOnO %s \n" % numberText)
                print("GOOOOOD NUMBER")

            elif xxyyiiss(intNumber) == True:
                fajl.write("xxyyiiss %s \n" % numberText)
                print("GOOOOOD NUMBER")
                
            elif nnx0x0(intNumber)==True: 
                fajl.write("nnx0x0 %s \n" % numberText)
                print("GOOOOOD NUMBER")
                
            elif xyxynO(intNumber)==True:
                fajl.write("xyxynO %s \n" % numberText)
                print("GOOOOOD NUMBER")    
                
            elif xOxOxO(intNumber)== True:
                fajl.write("xOxOxO %s \n" % numberText)
                print("GOOOOOD NUMBER")
                
            elif nOnOnO(intNumber) == True:
                fajl.write("nOnOnO %s \n" % numberText)
                print("GOOOOOD NUMBER")     
                
                
            elif xxxxxx(intNumber)==True:
                fajl.write("xxxxxx %s \n" % numberText)
                print("GOOOOOD NUMBER")
                
                
            elif increasing1reducing(intNumber)==True:
                fajl.write("increasing1reducing %s \n" % numberText)
                print("GOOOOOD NUMBER")
                
                
            elif increasing5reducing(intNumber)==True:
                fajl.write("increasing5reducing %s \n" % numberText)
                print("GOOOOOD NUMBER")    
                
            elif xxxyyy(intNumber)==True:
                fajl.write("xxxyyy %s \n" % numberText)
                print("GOOOOOD NUMBER")
            elif  xysxys(intNumber)==True:
                fajl.write("xysxys %s \n" % numberText)
                print("GOOOOOD NUMBER")
                
            elif xxOOOO(intNumber)==True:
                fajl.write("xxOOOO %s \n" % numberText)
                print("GOOOOOD NUMBER")
            elif xyxyxy(intNumber)==True:
                fajl.write("xyxyxy %s \n" % numberText)
                print("GOOOOOD NUMBER")
            elif ssxyxyxs(intNumber)==True:
                fajl.write("ssxyxyxs %s \n" % numberText)
                print("GOOOOOD NUMBER")
                
            elif xyxyss(intNumber)==True:
                fajl.write("xyxyss %s \n" % numberText)
                print("GOOOOOD NUMBER")
                
            else:
            print("it s not good number")
        fajl.close()
       
    driver.close()


if __name__ == "__main__":
    while True:
        main()
        sleep(5)
    
