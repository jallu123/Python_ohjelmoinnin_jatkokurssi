# Vera Jalava
# 2520405

class Kurssisuoritus():
    def __init__(self, nimi: str, pisteet: int, arvosana: int):
        self.nimi = nimi
        self.pisteet = pisteet
        self.arvosana = arvosana
    def __repr__(self):
        return f"{self.nimi}, {self.pisteet} op, arvosana {self.arvosana}"
    def __eq__(self, other):
        return self.nimi == other.nimi and self.pisteet == other.pisteet

class suoritusote():
    def __init__(self, nimi: str):
        self.nimi = nimi
        self.suoritukset = []
    def __repr__(self):
        return f"{self.nimi}: {self.suoritukset}"

    def lisaasuoritus(self, uusisuoritus: Kurssisuoritus):
        for suoritus in self.suoritukset:
            if suoritus == uusisuoritus:
                if uusisuoritus.arvosana > suoritus.arvosana:
                    suoritus.arvosana = uusisuoritus.arvosana
                return

        self.suoritukset.append(uusisuoritus)

    def opintopisteet(self):
        summa = 0
        for suoritus in self.suoritukset:
            summa += suoritus.pisteet
        return summa

    def keskiarvo(self):
        summa = 0
        for suoritus in self.suoritukset:
            summa += suoritus.arvosana
        return summa / len(self.suoritukset)

    def painotettukeskiarvo(self):
        summa = 0
        pisteet = 0
        for suoritus in self.suoritukset:
            summa += suoritus.arvosana * suoritus.pisteet
            pisteet += suoritus.pisteet
        return summa / pisteet

suoritusote = suoritusote("Vera")


while True:
    print("Anna kurssin nimi (lopeta lopettaa): ")
    kurssin_nimi = input()

    if kurssin_nimi == "lopeta":
        break

    pisteet = int(input("Anna opintopisteet: "))
    arvosana = int(input("Anna arvosana: "))

    uusisuoritus = Kurssisuoritus(kurssin_nimi, pisteet, arvosana)

    suoritusote.lisaasuoritus(uusisuoritus)


print(suoritusote)
print("Opintopisteet: ", suoritusote.opintopisteet())
print("Keskiarvo: ", suoritusote.keskiarvo())
print("Painotettu keskiarvo: ", suoritusote.painotettukeskiarvo())