import os

# Dictonaries
# -------------

# Dictonary method 'get'

pairs = {1: 'apple',
         "orange": [2, 3, 4],
         True: False,
         None: "True", }

print (pairs.get("orange"))
print (pairs.get(7))
print (pairs.get(12345, "not in dictionary"))
os.system('cls')

# Tuples - krotki -  it is immutable (cannot be changed), list and dict can be changed.
words = ("spam", "eggs")
print (words[0])
# words[1] = "orange"

# List spices - like range, 1st arg is included in result, last isnt
# slicing working on tuples too, look down
squares = [0, 2, 3, 4, 5]
print (squares[0:2])

# tip - to reverse all list use mylist[::-1]

