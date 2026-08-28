nimi = "Kake"
syntymavuosi = 1967
opintopisteet = 67

s = f"Vuonna {syntymavuosi+2} syntyneellä {nimi}lla on {opintopisteet} opintopistettä"

s += "!"

print(f"{s}!!")


while True:
    nimi = input("Anna nimesi: ")
    if nimi == "lopeta":
        break
    elif nimi == "kake":
        continue
    else:
        print(f"Terve {nimi}!")

