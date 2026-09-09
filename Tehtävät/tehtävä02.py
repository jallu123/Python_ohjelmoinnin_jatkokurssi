# Vera Jalava
# 2520405

def laske_opintopisteet(kurssit):
    summa = 0
    for kurssi in kurssit:
        summa += kurssi["op"]
    return summa

def laske_keskiarvo(kurssit):
    summa = 0
    for kurssi in kurssit:
        summa += kurssi["arvosana"]
    return summa / len(kurssit)

def laske_painotettu(kurssit):
    summa = 0
    opintopisteet = 0

    for kurssi in kurssit:
        summa += kurssi["arvosana"] * kurssi["op"]
        opintopisteet += kurssi["op"]

    return round(summa / opintopisteet, 1)

kurssit = []

while True:
    nimi = input("Anna kurssin nimi (lopeta lopettaa): ")

    if nimi == "lopeta":
        break

    op = int(input("Opintopisteet: "))

    if op < 0 or op > 20:
        print("Virheellinen syöte.")
        continue

    arvosana = int(input("Arvosana: "))

    if arvosana < 1 or arvosana > 5:
        print("Virheellinen syöte.")
        continue

    kurssi = {
        "nimi": nimi,
        "op": op,
        "arvosana": arvosana
    }

    kurssit.append(kurssi)

print("Opintopisteet yhteensä", laske_opintopisteet(kurssit))
print("Suoritetut kurssit:")

numero = 1

for kurssi in kurssit:
    print(f"{numero}. {kurssi['nimi']}({kurssi['op']}op): {kurssi['arvosana']}")
    numero += 1


if len(kurssit) > 0:
    print("Arvosanojen keskiarvo:", laske_keskiarvo(kurssit))
    print("Arvosanojen painotettu keskiarvo:", laske_painotettu(kurssit))



