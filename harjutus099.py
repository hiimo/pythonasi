#hiimo närep
#1.11.22
#harjutus09
import locale
import datetime

#tekitame kuupäev
aeg = datetime.datetime.now()
print(aeg.strftime(" %d, %B, %Y"))

locale.setlocale(locale.LC_ALL, "et_EE")
aeg = datetime.datetime.now()
print(aeg.strftime(" %d, %B, %Y"))

id="50606187050"
#print(id[1:7])
sp = datetime.date(int("20"+id[1:3]), int(id[3:5]), int(id[5:7]))
print(sp)

print(aeg.year-sp.year)



