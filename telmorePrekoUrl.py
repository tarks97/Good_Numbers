import urllib.request
import json
from algoritmi import *
from myemail import send_numbers


def getTelmore():
    with urllib.request.urlopen("https://www.telmore.dk/api/common/anumber/numberbatch?cacheBuster=1571590678953") as url:
        phoneNumbers = json.loads(url.read().decode())
        numbers = set()  # Skup(nema duplikata)
        with open("telmore.txt", "+a",) as fajl:
            for phoneNumber in phoneNumbers:
                numberText = phoneNumber['phoneNumber']
                try:
                    intNumber = int(numberText)
                except:
                    continue
                numbers.add(numberText)
                print(numberText)
                                                                                                    #radi                                                                                                                                                                         #ova radi xx0000                             
                if xxxyyyincreasingone(intNumber) == True:
                    fajl.write("xxxyyyincreasingone  %s \n" % numberText)
                    print("GOOOOOD NUMBER")
                    send_numbers(numberText)
                    
                    
                elif ThreeZeros(intNumber) == True: 
                    fajl.write("ThreeZeros %s \n" % numberText)
                    print("GOOOOOD NUMBER")
                    send_numbers(numberText)
                    
                elif nnoOneTwoThreeFourFiveSix(intNumber) == True:
                    fajl.write("nnoOneTwoThreeFourFiveSix %s \n" % numberText)
                    print("GOOOOOD NUMBER")
                    send_numbers(numberText)
                
                elif nnxyxy(intNumber) == True:
                    fajl.write("nnxyxy %s \n" % numberText)
                    print("GOOOOOD NUMBER")
                    send_numbers(numberText)
                elif nnoonetwothreefour(intNumber) == True:
                    fajl.write("nnoonetwothreefour %s \n" % numberText)
                    print("GOOOOOD NUMBER")
                    send_numbers(numberText) 
                elif nnxxxx(intNumber) == True:
                    fajl.write("nnxxxx %s \n" % numberText)
                    print("GOOOOOD NUMBER")
                    send_numbers(numberText) 
                elif  increasing25reducing(intNumber) == True:
                    fajl.write("increasing25reducing %s \n" % numberText)
                    print("GOOOOOD NUMBER")
                    send_numbers(numberText) 
                elif increasing50reducing(intNumber) == True:
                    fajl.write("increasing50reducing %s \n" % numberText)
                    print("GOOOOOD NUMBER")
                    send_numbers(numberText) 
                elif  increasing10reducing(intNumber) == True:
                    fajl.write("increasing10reducing %s \n" % numberText)
                    print("GOOOOOD NUMBER")
                    send_numbers(numberText)
                elif increasing2reducing(intNumber) == True: 
                    fajl.write("increasing2reducing %s \n" % numberText)
                    print("GOOOOOD NUMBER")
                    send_numbers(numberText) 
                    
                elif increasingFourreducing(intNumber) == True:
                    fajl.write("increasingFourreducing %s \n" % numberText)
                    print("GOOOOOD NUMBER")
                    send_numbers(numberText) 
                elif nOnnnOnO(intNumber) == True:
                    fajl.write("nOnnnOnO %s \n" % numberText)
                    print("GOOOOOD NUMBER")
                    send_numbers(numberText)
                elif xxyyiiss(intNumber) == True:
                    fajl.write("xxyyiiss %s \n" % numberText)
                    print("GOOOOOD NUMBER")
                    send_numbers(numberText) 
                elif nnx0x0(intNumber)==True: 
                    fajl.write("nnx0x0 %s \n" % numberText)
                    print("GOOOOOD NUMBER")
                    send_numbers(numberText) 
                elif xyxynO(intNumber)==True:
                    fajl.write("xyxynO %s \n" % numberText)
                    print("GOOOOOD NUMBER")    
                    send_numbers(numberText) 
                elif xOxOxO(intNumber)== True:
                    fajl.write("xOxOxO %s \n" % numberText)
                    print("GOOOOOD NUMBER")
                    send_numbers(numberText) 
                elif nOnOnO(intNumber) == True:
                    fajl.write("nOnOnO %s \n" % numberText)
                    print("GOOOOOD NUMBER")     
                    send_numbers(numberText) 
                    
                elif xxxxxx(intNumber)==True:
                    fajl.write("xxxxxx %s \n" % numberText)
                    print("GOOOOOD NUMBER")
                    send_numbers(numberText) 
                    
                elif increasing1reducing(intNumber)==True:
                    fajl.write("increasing1reducing %s \n" % numberText)
                    print("GOOOOOD NUMBER")
                    send_numbers(numberText) 
                    
                elif increasing5reducing(intNumber)==True:
                    fajl.write("increasing5reducing %s \n" % numberText)
                    print("GOOOOOD NUMBER")    
                    send_numbers(numberText) 
                elif xxxyyy(intNumber)==True:
                    fajl.write("xxxyyy %s \n" % numberText)
                    print("GOOOOOD NUMBER")
                    send_numbers(numberText) 
                elif  xysxys(intNumber)==True:
                    fajl.write("xysxys %s \n" % numberText)
                    print("GOOOOOD NUMBER")
                    send_numbers(numberText) 
                elif xxOOOO(intNumber)==True:
                    fajl.write("xxOOOO %s \n" % numberText)
                    print("GOOOOOD NUMBER")
                    send_numbers(numberText) 
                elif xyxyxy(intNumber)==True:
                    fajl.write("xyxyxy %s \n" % numberText)
                    print("GOOOOOD NUMBER")
                    send_numbers(numberText) 
                elif ssxyxyxs(intNumber)==True:
                    fajl.write("ssxyxyxs %s \n" % numberText)
                    print("GOOOOOD NUMBER")
                    send_numbers(numberText) 
                    
                elif xyxyss(intNumber)==True:
                    fajl.write("xyxyss %s \n" % numberText)
                    print("GOOOOOD NUMBER")
                    send_numbers(numberText) 
                    
                  
                else:               
                    print("not good number")
            
            fajl.close()
