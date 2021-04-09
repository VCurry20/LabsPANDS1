# Week 8 - Lab Question 2  --> working with numpy

# Write a prog that makes a list, called Salaries, that has 10 ransom number between 20000 - 80000
# modify the program so that random salaries is the same each time the program is run

import numpy as np

# it is a good idea to have absolute values set into variables at the beginning of your program

minSalary = 20000
maxSalary = 80000
numberOfEntries = 10

np.random.seed(1)       # keeps the random output the same 

salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)

print (salaries)