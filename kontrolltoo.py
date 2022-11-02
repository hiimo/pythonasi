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
    




