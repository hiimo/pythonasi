#Hiimonärep
#27.10.2022
#ül6

#1ül

failike=open("s6pru_l6ustaraamatus.txt", "r")

reformikaid = 0
keskerakond = 0
erakonnad = []

for i in (failike.readlines()):
    ee,pp,er,kyl = i.split(" ")
    if er=="RE":
        reformikaid+=1
    elif er=="KE":
        keskerakond+=1
    if er not in erakonnad:
        erakonnad.append(er)
    with open ("uusfail.txt","a") as fail_kirjutamiseks:
        fail_kirjutamiseks.write(ee+" "+pp+'\n')   
    
        
print(erakonnad)
print(f"keskerakond pls {keskerakond}")
print(f"reformikaid kokku {reformikaid}")
print(f"erakondi kokku (len{erakonnad})")
failike.close()




