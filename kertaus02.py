# #### Reading input
#
# In Python input from the user can be read by input() statement.
# Note that input() returns a string, so it must be converted to for example int for calculations.
#

#name = input("What is your name? ") # remove # in the beginning of line to try out
name = "Olli"
print("Hello,", name)
credits_input = input("How many credits do you have? ") # remove # in the beginning of line to try out
credits = int(credits_input)
print(type(credits_input), type(credits))
print(name, "has", credits, "credits.")
