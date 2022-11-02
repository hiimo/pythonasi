#hiimo
#2.11.22
#10harjtuts
import re



fh = open("C:/Users/it22/Desktop/juut.txt")
for line in fh:
     if re.search('^[A-Z0-9]+[A-Z]{1}', line):
         print(line,end='')



fh = open("C:/Users/it22/Desktop/juut.txt")
for line in fh:
    if re.search('\.[0,1]{1,8}\.[0,1]{1,8}\.[0,1]{1,8}\.[0,1]{1,8}$'):
         print(line,end='')

