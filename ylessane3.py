#Hiimo Närpe
#11.10.2022
#harjutus3

#korraliknimi
nimi = input("Sisesta nimi")
puh_nimi = nimi.strip().capitalize()

print("Tere,", puh_nimi+"!")

#vandumine
vannu = input("Vannu siis 'Kurat küll:' ")
print(vannu.lower().replace("kurat","*****"))

#email
email = input("Sisesta email kontrollimiseks: ")
print("@" in email)

#tundide ajad
algus = "8:30"
lopp = "14:15"

hh1,mm1 = algus.split(":")
minut1 = int(hh1)*60+int(mm1)
hh2,mm2 = lopp.split(":") #tteb pooelks
minut2 = int(hh2)*60+int(mm2) #arvutab
print(minut1,minut2) #naitab minutid
minutid = minut2-minut1 #ajavahe
hh = minutid//60
mm = minutid%60
print (f"Ajaline vahe on {hh}:{mm}")

#palindroom
def isPalindrome(h):
    return h == h[::-1]

h = input("sisesta palindroom: ")
ans = isPalindrome(h)

if ans:
    print("jah")
else:
        print("ei")

