# This program prints out fruit from a list of given fruits
# Also see random generator

import random

fruits = [ "Apple", " Orange", "Raspberry", "Pear", "Melon"]

# we want a random number between 0 and length -1

index = random.randint(0,len(fruits)-1)

fruit = fruits[index]
print(" A Random Fruit: {}".format(fruit))


## the list is written with index = random.randint(0,len(fruits)-1) - this will ensure if you add more to the list it will choose from it 
## where as it you write index = ransom.randint(0,5) it will only choose from the 5
## the first option gives your program more flexibilty

## index = ransom.randint(0,4) - this means all the fruits from 0 , 1, 2, 3 , 4 
## index = random.randint(0,len(fruits)-1) - this means all the items on the list (5) -1) = 0-4 = 0,1,2,3,4
## index lists start with 0 and not 1

