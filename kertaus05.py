# #### Combining conditions: and, or, not
# .
# Often the conditions for branching (and looping as well) need to combine several variable
# values. The connectives "and" and "or" can be used for combining two or more conditions
# and "not" for negating a condition.
#

credits = 45
average = 4.2
years = 2

if credits > 40 and average > 4.0 and years < 3:
    print("well done")

if years >= 3 and not credits > 40:
    print("speed-up needed")
else:
    print("looks ok")

# #### Loops - break and continue
#
# Looping can be ended before the loop condition becomes false by break. It also possible
# to skip further processing for one round with continue. These should be used sparingly.

for temperature in range(-3,3):
    print("Temperature", temperature)
    if temperature == 0:
        break

print("Again.")

for temperature in range(-3,3):
    print("Temperature", temperature)
    if temperature == 0:
        continue
    if temperature < 0:
        print("Hrr.")
    else:
        print("ok.")
