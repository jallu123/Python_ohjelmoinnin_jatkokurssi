# Tehtävä 1 : Opintolaskuri

# nimi = Vera Jalava
# opiskelijanumero = 2520405

kurssitulostus = ""
kurssien_maara = 0
pisteiden_summa = 0
arvosanojen_summa = 0
painotettu_summa = 0

while True:
    nimi = input("Kurssin nimi (lopeta lopettaa): ")
    if nimi == "lopeta":
        break

    opintopisteet = int(input("Opintopisteet: "))
    if opintopisteet < 0 or opintopisteet > 20:
        print("Virheellinen syöte")
        continue

    arvosana = int(input("Arvosana: "))
    if arvosana < 1 or arvosana > 5:
        print("Virheellinen syöte")
        continue

    kurssien_maara = kurssien_maara + 1
    pisteiden_summa = pisteiden_summa + opintopisteet
    arvosanojen_summa = arvosanojen_summa + arvosana
    painotettu_summa = painotettu_summa + opintopisteet * arvosana

    kurssitulostus = kurssitulostus + f"{kurssien_maara}. {nimi}({opintopisteet}op): {arvosana}\n"

if kurssien_maara > 0:
    keskiarvo = arvosanojen_summa / kurssien_maara
    painotettu_keskiarvo = painotettu_summa / pisteiden_summa

else:
    keskiarvo = 0
    painotettu_keskiarvo = 0

print("Opintopisteet yhteensä: ", pisteiden_summa)

if kurssien_maara > 0:
    print("Suoritetut kurssit: ")
    print(kurssitulostus)
    print(f"Arvosanojen keskiarvo: {keskiarvo:.1f}")
    print(f"Arvosanojen painotettu keskiarvo: {painotettu_keskiarvo:.1f}")









