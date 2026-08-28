# Sanakirja (Dictionary, Map): kokoelma avain-arvo -pareja.

numerot = {}
numerot["nolla"] = 0
numerot["yksi"] = 1
numerot["kaksi"] = 2
numerot["two"] = "kaksi"
numerot["kolme"] = 3
numerot["neljä"] = 4
numerot["viisi"] = 5
numerot["kuusi"] = 6
numerot["seitsemän"] = 7
numerot["kahdeksan"] = 8
numerot["yhdeksän"] = 9
print(numerot)

luku = ["neljä", "two", "kahdeksan", "nolla"]
for numero in luku:
    print(numerot[numero], end="")
print()

oprekisteri = {}
oprekisteri["Pirkko"] = [3,4,3,5,5]
oprekisteri["Pekka"] = [1,2,3,2,4,4,4,2,5]
oprekisteri["Paula"] = [1,2,3,4,4,2,5]
oprekisteri["Paavo"] = [1,3,2,5,5,4,2,5]

print(oprekisteri)
oprekisteri["Paavo"] = [1]
print(oprekisteri)
print(oprekisteri["Pekka"])

kaikkiensumma = 0
kaikkienmaara = 0
for op in oprekisteri:
    s = sum(oprekisteri[op])
    kaikkiensumma += s
    n = len(oprekisteri[op])
    kaikkienmaara += n
    print(f"{op}: {s/n:.1f}")
print(f"Kaikki: {kaikkiensumma/kaikkienmaara:.1f}")

def lisaasuoritus(nimi, arvosana, oprekisteri):
    if nimi in oprekisteri:
        oprekisteri[nimi].append(arvosana)

lisaasuoritus("Paavo", 1, oprekisteri)
lisaasuoritus("Kake", 5, oprekisteri)
print(oprekisteri)

def lisaasuoritusturbo(nimi, arvosana, oprekisteri):
    if not nimi in oprekisteri:
        oprekisteri[nimi] = []
    oprekisteri[nimi].append(arvosana)

lisaasuoritusturbo("Päivi", 5, oprekisteri)
lisaasuoritusturbo("Paavo", 2, oprekisteri)
print(oprekisteri)

oprekisteri.pop("Päivi")
print(oprekisteri)

# Aikaisemmin määriteltiin opiskelija tähän tyyliin:
op1 = ["Pirkko", 44, [3,4,3,5,5]]
op2 = ["Pekka", 33, [1,2,3,2,4,4,4,2,5]]

# Parempi esitystapa
op1 = {"nimi": "Pirkko", "ika": 44, "arvosanat": [3,4,3,5,5]}
op2 = {"nimi": "Pekka", "ika": 33, "arvosanat": [1,2,3,2,4,4,4,2,5]}
rekisteri = [op1, op2]
print(rekisteri)
print("Keski-ikä", (rekisteri[0]["ika"] + rekisteri[1]["ika"])/2 )
