#tünis käandmaa
#25.10.22
#Ul5 vmdgi

#tärnid

import random

#vanus
vanus = (random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),)

for kaka in vanus:
    print(f"{kaka*'*'}")


import random
import statistics
#vanus
vanus = (random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),)
print(vanus)
print(min(vanus))
print(max(vanus))
print(sum(vanus))
print(round(sum(vanus)/7))


#duplikaadid


inimesed = ["Juhan","Kati","Mario","Mati","Mati"]
myopilased =set(inimesed)
print(myopilased)


#õpilased
jrk = 1
opilased = ["Juhan","Kati","Maarja","Mario","Mati"]
for opilane in opilased:
    print(f"{jrk}. {opilane}")
    jrk+=1
arv = int(input("mitmes nimi: "))-1

nimi = input("lisa uus nimi: ")
del opilased[arv]
opilased.insert(arv, nimi)
print(opilased)



#nimede lisamine

nimed = []
for i in range(5):
    nimi = input("lisa nimi: ")
    nimed.append(nimi)
print(f"viimane nimi: {nimed[-1]}")
nimed.sort()
print(nimed)