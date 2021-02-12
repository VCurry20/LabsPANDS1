# This program prints out fruit from a list of given fruits
# Also see random generator

import random

fruits = [ "Apple", " Orange", "Raspberry", "Pear", "Melon"]

# we want a random number between 0 and length -1

index = random.randint(0,len(fruits)-1)

fruit = fruits[index]
print(" A Random Fruit: {}".format(fruit))
