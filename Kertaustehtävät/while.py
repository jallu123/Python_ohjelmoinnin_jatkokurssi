# Tehdään summaus

summa = 0

while(True):
    syote = input("? ")
    if syote == ("done"):
        break
    syote_input = int(syote)
    summa = syote_input + summa


print(summa)

