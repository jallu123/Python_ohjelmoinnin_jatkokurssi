# ### Expressions
#
# Operators +, -, *, / and ** (power) work as expected. Division is always floating-point.
# Integer division operator is // and modulo (reminder) operator %. To ensure intended order
# of evaluation, use parethesis.
#
# Right-hand side of an assignment can be an expression. The value of the right-hand side
# expression is first evaluated (computed), and then assigned to be the new value for variable.
#
# Note that floating point artihmetic is not precise - floating point numbers represented
# in limited amount of memory cause rounding errors.
#
# Some of the operators (+ and * for string and integer) work with strings, too. + is
# string concatenation (gluing two strings together) and * is string repetition.
#
credits = 43
anotherName = "Jane Doe"
anotherCredits = 25
anotherAverage = 4

# assign value to variable: first evaluate right-hand side of assignment, the assign
# the resulting value to the variable
anotherCredits = anotherCredits + 5

creditsSum = credits + anotherCredits
creditsAverage = (credits + anotherCredits) / 2 # here parethesis are mandatory to get the intended result

print("creditsSum", creditsSum, "creditsAverage", creditsAverage)

exampleFloat = 100
exampleFloat = exampleFloat * 1.1
print(exampleFloat) # note that the result is not == 110 - this is because of rounding

passengers = 11
seatsPerCar = 4
fullCars = passengers // seatsPerCar # integer division
leftOver = 11 % 4 # reminder

print("Full cars", fullCars, "leftovers", leftOver)

firstName = "Albert"
lastName = "Einstein"
wholeName = firstName + " " + lastName
wholeNameJamesBondStyle = lastName + ", " + wholeName

print("Whole name", wholeName, "or", wholeNameJamesBondStyle)
print(firstName*4)

# #### Short-hand expressions
#
# Doing an arithmetic operation with a variable can be combined with assignment
# with shorthand: age += 1 is the same as age = age + 1. This works with all relevant operators.

age = 35
weight = 77
print(age, weight)

age += 1 # increase age by one; or age = age + 1
weight *= 1.1 # weight gets multiplied by 1.1; or weight = weight * 1.1

print(age, weight)