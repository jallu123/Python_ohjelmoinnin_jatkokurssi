a = 1
b = 2
print("Viittaus a:han", id(a), "Viittaus b:hen", id(b))
a = b
print("Viittaus a:han", id(a), "Viittaus b:hen", id(b))


m1 = [1,3,5]
m2 = m1 # tämän jälkeen m1 ja m2 viittaavat samaan listaan
print("id(m1)",id(m1), "id(m2)", id(m2))

m1.append(7)
m2.append(9)
print("m1",m1)
print("m2",m2)
print("id(m1)",id(m1), "id(m2)",id(m2))

m2 = m1[:] # m2:een sijoitetaan viittaus m1:n kopioon
m2.append(11)
print("m1",m1)
print("m2",m2)
print("id(m1)",id(m1), "id(m2)",id(m2))

def nollaanegatiiviset(numerot: list):
    i = 0
    while i < len(numerot):
        if numerot[i] < 0:
            numerot[i] = 0
        i += 1

nums = [-2,5,6,7,-9,-1,5]
nollaanegatiiviset(nums)
print(nums)

def poistanegatiiviset(numerot: list):
    tuloslista = []
    for num in numerot:
        if num >= 0:
            tuloslista.append(num)
    numerot[:] = tuloslista # kokeile numerot = tuloslista; miksi ei toimi?

nums = [-2,5,6,7,-9,-1,5]
poistanegatiiviset(nums)
print(nums)
