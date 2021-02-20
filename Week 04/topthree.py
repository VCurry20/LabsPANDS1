# labs 4.2

# Write a program that generates 10 random numbers (0-100),
# prints them out 
# then prings the top three

# **** new concepts in this lab / not yet covered ****


# This program generates 10 random numbers
# prints them out, then
# prints the top 3

# I will use a list to store and 
# manipulate the numbers

import random  # I program the general case ( dunnno what this means)

howmany = 10
tophowmany = 3
rangeFrom = 0 
rangeto = 100

numbers = []

for i in range (0,10) :
    numbers.append(random.randint(rangeFrom,rangeto))
print ("{} random numbers\t {}".format(howmany,numbers))

# I am keeping the original list maybe I don't need to 
# I got the itea to sort and split the list from stackover flow 

topones = numbers.copy()
topones.sort(reverse=True)
print ("The top {} are \t\t {}".format(tophowmany, topones[0:tophowmany]))
