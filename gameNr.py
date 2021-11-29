import re

with open('solo.txt', 'r') as f1, open('data/test.txt','a') as f2:
    #x = f.readlines()
    for i in f1:
        x= f1.readline(17)
        y= x.split("][")
        #print(y[0])
        str1= str(y)[1:-1]
        str2 = str1[1:-1]
        #print(str2)
        new = str2.replace('GameNr', '')
        new1 = new.replace('[', '')
        new2 = new1.replace(']', '')
        new3 = new2.replace('"', '')

        #if not new3.isspace():
        if not new3.strip():
            continue
        if new3:

        #new3.replace(' ', '')
        #print(new3)
            f2.write(new3 + '\n')

