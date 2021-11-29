import re
import json

#Read the text file
f = open("../data/solo.txt","r")
string = f.read()

#1) split file into unnecessary & necessary parts
start='1.'
end='['

unnec_code =  [i for i in string.split(start, 1)]
until_code = [start+i for i in unnec_code[1].split('[',1)]

info_code = unnec_code[0]
rounds_code = until_code[0]

#Info header information
info = re.findall(r'(\[\w+ \"[^"]+\"])',info_code)

#creating diciontary
jsonString = {}

#Putting the header into the JSON-string
for i in info:
    detail = re.sub(r"[\[\]\"]","",i)
    string = detail.split(' ',1)
    jsonString[string[0]] = string[1]

#Splitting every round with the the round number
rounds = re.split(r'(\d\.\s)',rounds_code)
#removing the empty string in the list
del rounds[0]
#Putting the round number with the round together
full_rounds = [rounds[i-1]+rounds[i] for i in range(len(rounds)) if (i % 2) != 0]

#EAnalyzing every move, round, time and putting them into JSON
jsonString['Chess_Rounds'] = []

for loop in full_rounds:
    round_nr = re.search(r'(\d)\.', loop)
    move = re.findall(r'\s([A-Za-z0-9-]+)\s', loop)
    time_date = re.findall(r'\{ ([A-Za-z0-9-=:. ]+)}', loop)

    round_nr = int(round_nr.group(1))
    move = move
    time_date = [t[:-1] for t in time_date]
#putting data into Json
    jsonString['Chess_Rounds'].append({
        'round_nr': round_nr,
        'moves': move,
        'time_date': time_date
    })
#Converting from dictionary into JSOn
jsonString = json.dumps(jsonString, indent=4)

#print(jsonString)
with open("solo_JSON.json", "w") as JSONWriter:
    JSONWriter.write(jsonString)

