"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730318766"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
rand_fortune: int = int(randint(1,5))

print("Your fortune cookie says...")

if rand_fortune == 1:
    print("A truly rich life contains love and art in abundance.")
else:
    if rand_fortune == 2:
        print("One can never fill another’s shoes, rather he must outgrow the old shoes.")
    else:
        if rand_fortune == 3:
            print("Soon life will become more interesting.")
        else:
            if rand_fortune == 4:
                print("Your love life will be happy and harmonious.")
            else:
                if rand_fortune == 5:
                    print("You will be sharing great news with all the people you love.")

print("Now, go spread positive vibes!")
