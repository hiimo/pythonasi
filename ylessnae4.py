#Hiimo Närep
#17.10.2022
#ylesane4

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
vanus = input("sisesta vanus: ")
print(vanus)
if vanus=="5":
    vastus = vanus / "5"
    print("juubel")
else:
    print("pole juubel")
