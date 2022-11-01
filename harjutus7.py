#hiimo närep
#1.11.22
#harjutus07

import math



#funktsiooni loomine
def teavita(a):
    print(f"tere {a}")
teavita("juut")



#oma funktsiooni loomine parameetritega
def tervita(a= "unknown", b= "ge"):
    if b=="et":
        print(f"tere {a}")
    elif b=="en":
        print(f"hi {a}")
    else:
        print(f"hallo {a}")
#kutsud funktsiooni välja
tervita("juut")

print("LEIAME RUUMALA")

#ruumala

def kuup(a):
    print(f"kuubi ruumala on {a**3}")

def kera(b):
    print(f"kera pindala on {4**math.pi**b}")

def koonus(r,h):
    print(f"koonuse ruumala on {round(math.pi*r**2)*h/3}")
    
def silinder(x2,x3):
    print(f"silindri ruumala on {round(math.pi*x2**2)*x3/3}")
    





loop = 1

while loop==1:
    print("vali kujund: \n1.kuup \n2.kera \n3.koonus \n4.silinder")
    kujund = int(input("lisa kujundi number 1-4: "))
    if kujund==1:
        x = int(input("sisesta kuubi raadius pikkus: "))
        kuup(x)
    elif kujund==2:
        x1 = int(input("sisesta kera raadius: "))
        kera(x1)
    elif kujund==3:
        r = int(input("sisesta koonuse kylje pikkus: "))
        h = int(input("sisesta kuubi kylje pikkus: "))
        koonus(r,h)
    elif kujund==4:
        x2 = int(input("sisesta raadius: "))
        x3 = int(input("sisesta pikkus: "))
        silinder(x2,x3)
    else:
        print("palun valige 1-4")



