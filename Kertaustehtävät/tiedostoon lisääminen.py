import json
import urllib.request

lue = urllib.request.urlopen("https://users.metropolia.fi/~peterh/kurssit.json")
data = lue.read()

print(data)
print(len(data))

kurssit = json.loads(data)
print(kurssit)
print(len(kurssit))

kurssit.append('{"nimi",:"Ontologia", "pisteet":16, "arvosana":5}')
print(len(kurssit))

with open('kurssit.json', 'w') as outfile:
    data = json.dumps(kurssit)
    outfile.write(data)


