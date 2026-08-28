nimet = ""

while True:
    syote = input("Anna nimesi: ")
    if syote == "lopeta":
        break
    nimet = nimet + syote + "\n"

print("Tulos on: ")
print(nimet)
