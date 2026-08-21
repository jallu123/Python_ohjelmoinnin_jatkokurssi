# ### Loops
#
# Loops allow us to repeadetly run some lines of code without having to retype each line.
# They are the basis for almost all data processing tasks and algorithms.
#

# #### for loop
#
# To repeat a section of code for a number of times, a loop can be used. In Python one way of
# looping is for() which together with range() gives a nice way for repetition. The for
# statement ends with colon ":", and all **indented** lines after that are repeated.
# A range(5) means a range of integer numbers starting from 0, and ending in 4 (= 5-1),
# ie. 0,1,2,3,4. range() accepts also starting point for the numeric range, range(5,10)
# gives the range 5,6,7,8,9. We will later use another kind of for loop to iterate
# through a collection of data items.
#
#

for temperature in range(10): # the loop is repeated 10 times, with temperature getting values 0,1,...,9
    print("Temperature is", temperature)
print("Now temperature is", temperature) # Note that this line is not repeated 10 times; it is not indented

for temperature in range(-5,5+1): # loop for temperature values from -5 to 5
    print("Temperature is", temperature)
print("The loop is over.")

# #### while loop
#
# In a while loop a condition is given to indicate whether the code in the loop should be
# executed or not. If the condition evaluates to true, the body of the loop is executed,
# and after that the condition is checked again. If the condition evaluates to false,
# the next line of code to be executed is after the last line of the loop (the last
# indented line).
#

temperature = -5
while temperature < 5:
    print("Temperature is", temperature)
    temperature += 1

print("The loop is over.")

# #### if - else
#
# The ability to branch based on truth value of a condition is another building block for
# writing efficient data processing algorithms.
#
# In Python a simple if-statement consist of if, floowed by a condition. If the condition
# is true, the indented lines of code following if-statement are run.
#
# The if-statement can optionally have an else-branch which is executed when the condition
# of the if statement is not true.
#
# Further branching is possible: the else branch can have an if part (elif) where another
# condition is given, and based on the truth value a branch of code is selected to be executed.
#

#temperature = input("What is the temperature? ") # remove # in the beginning of line to try out
temperature = "-7"

temperature = int(temperature)

if temperature < 0:
    print("It is freezing.")

print("temperature", temperature)

if temperature > 0:
    print("It is ok.")
else:
    print("It is not at all ok.")

if temperature > 0:
    print("It is ok.")
elif temperature < 0:
    print("It is freezing.")
else:
    print("I don't know!")

if temperature % 2 == 0: # temperature is an even number
    print("temperature is even")
else:
    print("temperature is odd")
