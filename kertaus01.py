# ### Variables, assignments and printing
#
# Variables hold, or "memorize" a value. Name of a variable starts by convention with
# lowercase letter (_ and uppercase letters are syntactically legal, too, but often against
# convention). Variable names can't have spaces in them.
#
# The value of a variable can be replaced by assigning a new value to it with assignment
# operator =.
#
# Unlike in some other programming languages, a variable may be assigned a value of a type
# different from its current type. Types of values include integer (for example 4, 9455, -23),
# float (for example 1.25, -67.9), boolean (True, False), and string ("Boris", "---", "64",
# "true", "23.6", ""). You can find out the type of a variable with type(). There are machanisms
# to convert values to different types, for example a string can be converted to an int by
# calling int(astring).
#
# print() can be used to output variable values, and constant values as well. If you wish to
# output several values on a same line, separate them with commas.

# some legal variable names are assigned values
credits = 25
name = "John Doe"
average = 3.5
active = True
# print out the values of the variables
print(credits, name, average, active)
# print out the types of the variables
print(type(credits), type(name), type(average), type(active))

# These would be illegal variable names:
# 5stars = 5
# large number = 1000

credits = 27 # old value 51 is now completely forgotten
credits = "many" # now the value of age is of type string
credits = "28" # this is leagal, and often confusing
credits = 28 # back to int value, the previous value "28" is now forgotten

# print out the values in a nicer way
print(name, "has now", credits, "credits.")
print(name, "has", credits, "with average", average)

print("Hello")
