#Hiimo Närep
#17.10.2022
#ylesane4
import random

#ruut
a = int(input("Sisesta kulg1: "))
b = int(input("Sisesta kulg2: "))
if a==b:
    print(f"{a} ja {b} moodustavad ruudu")
else:
    print(f"{a} ja {b} moodustavad ristküliku")

#matemaatika
nr1,nr2 = 9,4
tehe = input("vali tehe (* / + -):")

if tehe=="*":
    vastus = nr1 * nr2
elif tehe=="/":
    vastus = nr1 / nr2
elif tehe=="+":
    vastus = nr1 + nr2
elif tehe=="-":
    vastus = nr1 - nr2
    
else:
    vastus = "n/a"
    
    
    
print(f"{nr1}{tehe}{nr2}={vastus}")



#juubel
vanus1 = input("sisesta vanus: ")
print(vanus1)
if vanus1==0:
    vastus = (vanus1 / 5)
    print("juubel")
else:
    print("pole juubel")
    
    
    
#müük
hind = 24
if hind<=10:
    ale = 0.1
else:
    ale = 0.2
summa = hind-hind*ale

print(f"summa: {hind-hind*ale}")

#jalka
vanus = 17
sugu = "m"

if vanus>=16 and vanus<18 and sugu =="m":
    print("sobib meeskonda")
else:
    print("ei sobi")
    
#tärnid
nr = 8
for h in range(1,6):
    print("* " * nr)

arv = 5
for i in range(5):
    print("* " * arv)
    arv -= 1


#loto
for i in range (5):
    lamp = random.randint(0,5)
    print(lamp, end="")

#paaris ja paaritu
p = random.randint(1,10)
if p%2==0:
    print("on paaris", p)
else:
    print("ei ole paaris", p)
    
#korrutus tabel
    
    
#arvamis mäng
loop = 1
skoor = 0

while loop==1:
    suvarv = random.randint(1,10)
    print(suvarv) #test
    for i in range(3):
        valik = int(input("vali arv 1-10: "))
        if valik == suvarv:
            print("winner")
            skoor+=1
            break
        else:
            print("wrong")
    loop = int(input("Veel (1/0)? "))
print("game over")
print(f"skoor {skoor}")

#pank
konto = 10000
intress = 0.05
periood = 5

for i in range(1,periood+1):
    print(f"{i} {round(konto)} {round(konto*intress,2)} {round(konto+konto*intress)}")
    konto = konto+konto*intress
print(f"konto seis: (round(konto,2)}")
print(f"kasum: {round(konto-10000,2)}")

print()