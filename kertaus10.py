import math
# 2-tuple.
p1 = (4,3)
print("Etäisyys origosta", math.sqrt(p1[0]*p1[0] + p1[1]*p1[1]))

pelilauta = {}
pelilauta[(2,3)] = "kuningas"
pelilauta[(3,3)] = "lähetti"
print(pelilauta)

def tilastot(numerot: list):
    maara = len(numerot)
    summa = sum(numerot)
    return (summa/maara, min(numerot), max(numerot))

print(tilastot([1,4,2,5]))

p2 = 1,2 # sama kuin p2 = (1,2)

a = 6
b = 1

# vaihdetaan a:n ja b:n arvot keskenään
a, b = b, a
print(a, b)

tmp = a
a = b
b = tmp
