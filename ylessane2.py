#Hiimo Närep
#11.10.2022
#kolmnrk
import math
#tootehind

hind = 25.32
ale = 0.5
kogus = 5
summa = round((hind-hind*ale)*3,2)
print(kogus, "toote summa on",summa,"eurot")

#pitsa
pitsa = 12.90
sõbrad = 3
joot = 0.1
maks = (pitsa+pitsa*joot)/3
print(sõbrad,"pitsa jagame 3meks",maks,"eurot")

#rulluisutajad
keskmine = 29.9
aeg = 24
kaugus = round((keskmine*aeg)/60,2)
print("rulluisutajad jouvad",kaugus,"km")

#hüputeenus

a,b = 16,9
hs = math.sqrt(pow(a,2)+ b**2)
print("hüpoteenus on",hs)

#ajateisendus

aeg = int(input("Sisesta minutid"))
tunnid = aeg//60
minutid = aeg%60
print("vastus:",tunnid,":",minutid)

#arvusüsteemid

b = int(input("Sisesta täisarv:	"))
print("2ndsysteemis:",bin(b))
print("16ndsysteemis:",hex(b))


#kütusekulu arvutamine
tank = int(input("mitu liitrit"))
kilomeeter = int(input("mitu km"))
kulu = (tank/kilomeeter)/100
print("kytuse kulu on",kulu,"km")




#ümbermoot

a,b,c = 5,5,5
p = a + b + c
print("Kolmnurga ümbermoot on: ", p)