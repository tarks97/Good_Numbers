from algoritmi import *
 
with open("Dobribrojevi.txt", "+a",) as fajl:
    for i in range(31100000,31700000):
       if xxxyyyincreasingone(i) == True or nnx0x0(i)==True  or xyxynO(i)==True  or xOxOxO(i)== True  or nOnOnO(i) == True  or xxxxxx(i)==True or increasing1reducing(i)==True or increasing5reducing(i)==True  or xxxyyy(i)==True or xysxys(i)==True or xxOOOO(i)==True or xyxyxy(i)==True or ssxyxyxs(i)==True or xyxyss(i)==True:
           fajl.write("%s \n" % i)
           print("GOOOOOD NUMBER")
       else:               
            print("not good number")
                   
    fajl.close()

