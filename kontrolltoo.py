#hiimo
#2.11.22
#kontroltoo

fail = open("rebased.txt", encoding="UTF-8")
vastuvoetud = []
aastad = [2011,2012,2013.2014,2015,2016,2017,2018,2019]
for rida in fail:
    vastuvoetud.append(int(rida))
aasta = int(input("Mis aastat tahad? "))
index = aastad.index(aasta)
print(vastuvoetud[index])

fail.close()






m = int(input("mitu poialpossi tahab ounu? "))
u=0
for i in range (m):
    n=random.randint(1,2)
    print(n)
    u+=n
summa=14-u
print(summa)







#nisupask
nisuterade = 0.5
taisarv = int(input("sisesta taisarv: "))
j = 0
while j < taisarv:
    j += 1
    nisuterade *= 2

print(nisuterade)





#taring

taring = int(input("mitu taringut: "))
for i in range(taring):
    print(random.randint(1,6))



#murelikud lapsevanemad
ringid = int(input("ringide arv: "))
ring = 0
porgand = 0
while ring<ringid:
    ring +=1
    if  ring%2==0:
        porgand+=ring
print(f"porgand: {porgand}")


#aratus
aratus = int(input("ÄRATUS: "))
for i in range(aratus):
    print("tõuse ja sära")


#tervitus

print("Tere, maailm!")
import math

#bussid
inimesed = int(input("kui palju on inimesi bussis: "))
kohad = int(input("mitu kohta on bussis: "))
buss = (inimesed/kohad) 
print(f"busse on vaja {math.ceil(buss)}")
jaak = inimesed%kohad
if jaak==0:
    print("Buss on täis")
else:
    print(f"viimases bussis on {jaak}")




#liblikas

aasta = 2020
liblikas = "teelehe-mosaiikliblikas"
lause_keskosa = "aasta liblikas on"
lause = aasta,lause_keskosa,liblikas
print(lause)


#pilved
pilv = int(input("kui palju on pilvede aluse kõrgus (km) : "))

if pilv>=6:
    print("need on ylemised pilved")
else:
    print("pole ylemised pilved")
    




