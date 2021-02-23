"""Some examples of list concepts."""

rolls: list[int] # Declare a variable  whose type is list of ints

rolls = [2, 3, 2, 6] # Initialized w/ list literal syntax

print(f"Length of rolls is {len(rolls)}")
print(f"The last value in the list is {rolls[len(rolls) -1]}")

from random import randint
rolls.append(randint(1, 6)) #Lists's append method adds an item to the end of a list
print(rolls)

rolls.pop() # With no argument, removes the last item of the list
rolls.pop(0) # With one argument, removes specific index
print(rolls)

words: list[str] = list() # Construct an empty list using the list constructor
words.append("Hello")
print(words)
