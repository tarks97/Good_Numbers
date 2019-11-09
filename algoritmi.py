def xxxyyyincreasingone(broj):

    temp = broj % 1000
    broj = int(broj/1000)
    broj = broj % 1000
    if (temp-broj) == 1 or (temp-broj) == -1:
        return True
    return False

def xxxyyy(broj):
    temp = broj%1000
    broj = int(broj/1000)
    broj = broj%1000
    if temp%10==int(temp/10)%10 and int(temp/10)%10==int(temp/100)%10 and broj%10==int(broj/10)%10 and int(broj/10)%10==int(broj/100)%10:
        return True
    return False



def xysxys(broj):   

    temp = broj % 1000
    broj = int(broj / 1000)
    broj = broj % 1000
    if temp==broj:
        return True
    return False


def xyxyxy(broj):
    br3 = broj % 100
    broj = int(broj / 100)
    br2 = broj % 100
    broj = int(broj / 100)
    br1 = broj % 100
    broj = int(broj / 100)

    if br1==br2 and br3==br2:
        return True
    return False



def ssxyxyxs(broj):
     br3 = broj % 100
     broj = int(broj / 100)
     br2 = broj % 100
     broj = int(broj / 100)
     br1 = broj % 100
     broj = int(broj / 100)

     if  (br1 == br2) and (br3 % 10 == broj % 10) and (int(br3 / 10) % 10 == int(br1 / 10) % 10):
        return True
     return False
  
def xyxyss(broj):
      br3 = broj % 100
      broj = int(broj / 100)
      br2 = broj % 100
      broj = int(broj / 100)
      br1 = broj % 100
      broj = int(broj / 100)
      if br1 == br2 and br3 % 10 == br3 / 10 % 10:
           return True
      return False


def xxOOOO(broj):
    if broj % 10 == 0 and int(broj / 10) % 10 == 0 and int(broj / 100) % 10 == 0 and int(broj / 1000) % 10 == 0:
        return True
    return False


def increasing5reducing(broj):
      br3 = broj % 100
      broj = int(broj / 100)
      br2 = broj % 100
      broj = int(broj / 100)
      br1 = broj % 100
      broj = int(broj / 100)
      if (br3 - br2 == 5 or br3 - br2 == -5) and (br2 - br1 == 5 or br2 - br1 == -5) and br1 % 5 == 0:
          return True
      return False


def increasing1reducing(broj):
      br3 = broj % 100
      broj = int(broj / 100)
      br2 = broj % 100
      broj = int(broj / 100)
      br1 = broj % 100
      broj = int(broj / 100)
      if (br3 - br2 == 1 or br3 - br2 == -1) and (br2 - br1 == 1 or br2 - br1 == -1):
          return True
      return False


def xxxxxx(broj):  
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
    if br1 == br2 and br2 == br3 and br3 == br4 and br4 == br5 and br5 == br6:
        return True
    return False    


def nOnOnO(broj):
    if broj % 10 == 0:
       broj = int(broj / 100)
       if broj % 10 == 0:
          broj = int(broj / 100)
          if broj % 10 == 0:
              return True
    return False





def xOxOxO(broj):
      br3 = broj % 100
      broj = int(broj / 100)
      br2 = broj % 100
      broj = int(broj / 100)
      br1 = broj % 100
      broj = int(broj / 100)
      if br1 == br2 and br2 == br3 and br1 % 10 == 0 and br2 % 10 == 0 and br3 % 10 == 0:
          return True
      return False
def xyxynO(broj):      
      br3 = broj % 100
      broj = int(broj / 100)
      br2 = broj % 100
      broj = int(broj / 100)
      br1 = broj % 100
      broj = int(broj / 100)
      br4 = int(br3 / 10)
      
      if br1 == br2 and (br3 % 10 == 0 or br4 % 10 == 0):
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


#---------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------#

# NN XXXX,     NN XYXY    zadnja 4 broja- 1234,    123456 in the end,  any number with 3 zeros, 
# # -2 broja,  +2 broja, +4 broja, xx yy ii ss,  +10, +50, -50, n0 nn n0 n0, +-25

#xx yy ii ss, n0 nn n0 n0
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