nimilista = []

while True:
    nimi = input("Anna nimi: ")
    if nimi == "lopeta":
        break
    nimilista.append(nimi)

print(sorted(nimilista))