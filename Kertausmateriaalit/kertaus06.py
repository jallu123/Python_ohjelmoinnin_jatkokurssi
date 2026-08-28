# ### Lists
# .
# In Python list is the most popular way of keeping together number of related values,
# for example groceries to buy, grades from courses, student ids of students in a course etc.
#
# List elements can be iterated over by for loop. If needed, the elements can be accessed
# by their index, which starts from 0, using []. With indexing a while loop can be used for
# iterating over the list elements. len() return the number of elements in a list. For loop
# has a form that can be used when indices are of importance.
#

groceriesList = ["potatoes", "tomatoes", "bread", "butter"]
print(groceriesList)
print()

for item in groceriesList:
    print(item)
print()

print(groceriesList[ 2 ]) # "a cucumber"
print()

index = 0
while index < len(groceriesList):
    print(index, groceriesList[ index ])
    index += 1
print()

for index, item in enumerate(groceriesList):
    print(index, item)
print()

# ### Lists: adding and removing elements
#
# Elements can be added to a list: append(elem) adds to the end of the list, insert(pos,elem)
# adds elem at position pos, moving everything from pos onwards by one step.
#
# To remove element(s) from a list use one of:
#
# *   pop(index): remove element at index, all elements at higher indicies are moved by one step
# *   remove(elem): remove elem from list; index is not needed
#
# Lists can be concatenated by + operator.

groceriesList = ["potatoes", "tomatoes", "bread", "butter"]

groceriesList.append("juice")
print(groceriesList)

groceriesList.insert(0, "cookies")
print(groceriesList)

groceriesList = groceriesList + ["cheese", "ice cream"]
print(groceriesList)

groceriesList.pop(2)
print(groceriesList)

groceriesList.remove("butter")
print(groceriesList)

# ### Lists: useful functions

print(sorted(groceriesList))
print(groceriesList)
groceriesList.sort()
print(groceriesList)

groceriesList.reverse()
print("reversed", groceriesList)

print("juice" in groceriesList)
print("beer" in groceriesList)

numbers = [1,2,3,4,5]
print(sum(numbers))
print(min(numbers))
print(sum(numbers)/len(numbers))
