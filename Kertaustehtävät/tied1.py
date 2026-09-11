tiedostonimi = "koe1"

with open(tiedostonimi, "r") as kukkuu:
    teksti = kukkuu.read()
    print("Tiedostossa", tiedostonimi, "on", len(teksti), "merkkiä.")
    print("Alkusulkuja:", teksti.count("("))
    print("Printtejä:", teksti.count("print("))
