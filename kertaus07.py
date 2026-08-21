# ### Functions
# .
# It is often very useful to capsulate often-used code so that it can be used without
# copying it. This can be accomplished by writing a function.
#
# A function can have **parameter(s)** with which **values can be passed** to the function.
# A function may also **return a value**.
#
# Function definition starts with keyword "def", followed by list parameter names in parenthesis,
# and a colon ":". The lines after colon that belong to the body of the function must be indented.
# A value can be returned from a function with "return" statement.
#
# When a function is called, the parameters get initialized to values given in the call.
#

# studentStatus() is a function that takes three parameters:
# credits, average, years
# and returns the status of a student as a string
def studentStatus(credits, average, years):
    if credits > 45 * years:
        if average >= 3.0:
            return "good"
        else:
            return "ok"
    else:
        return "not too well"

# printEvensFirst() takes a list argument and produces no result
# Its side effect, however, is that it prints out numbers in its
# parameter list so that even numbers come before odd numbers.
# printEvensFirst() is used for side-effect only.
def printEvensFirst(list):
    for e in list:
        if e % 2 == 0:
            print(e)
    for e in list:
        if e % 2 == 1:
            print(e)

myStatus = studentStatus(55, 2.6, 1)
# inside function studentStatus() credits has value 55, average 2.6, and years 1
theirStatus = studentStatus(102, 4.7, 2)

print(myStatus, theirStatus)

arvosanat = [5,5,3,4,1]

def luku_listalla1(luvut: list, etsittava: int):
    for luku in luvut:
        if luku == etsittava:
            return True
        else:
            return False

print(luku_listalla1(arvosanat, 5)) # True, oikein
print(luku_listalla1(arvosanat, 3)) # False, väärin mutta miksi?
# korjaus: parametri luku -> etsittava
# mutta, ei toimi vieläkään, miksi?

# toimiva ratkaisu
def luku_listalla(luvut: list, etsittava: int):
    for luku in luvut:
        if luku == etsittava:
            return True
    return False

summa = sum(arvosanat)
maara = len(arvosanat)
ka = summa / maara
print(ka)
print(sum(arvosanat) / len(arvosanat))

# listan elementtien ei tarvitse olla keskenään samantyyppisiä
# (kuten monissa muissa ohjelmointikielissä)
op1 = ["Pirkko", 44, [3,4,3,5,5]]
op2 = ["Pekka", 33, [1,2,3,2,4,4,4,2,5]]

print("Keski-ikä", (op1[1]+op2[1]) / 2)

def aska(op: list): # oletetaan, että parametri on op1 ja op2 kaltainen lista
    arvosanat = op[2]
    return sum(arvosanat) / len(arvosanat)

def tulostatiedot(op: list): # oletetaan, että parametri on op1 ja op2 kaltainen lista
    print("Opiskelija", op[0], "keskiarvo", aska(op))

tulostatiedot(op1)
tulostatiedot(op2)

# koostetaan yksittäisiä opiskelijoita esittävistä listoista op1 ja op2
# lista vuosikurssin opiskelijoista
vuosikurssi = [op1, op2]
print(vuosikurssi)

# matriisin voi esittää listana listoja:
m1 = [[2,3], [3,4], [4,5]]

print(m1)
print(len(m1))
print(len(m1[0]))
print(len(m1[1]))
print(len(m1[2]))
print(m1[2][1])

for rivi in m1:
    rivisumma = 0
    for num in rivi:
        rivisumma += num
    print(rivi, "summa", rivisumma)
