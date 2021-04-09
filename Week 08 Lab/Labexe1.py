# Week 8 - Lab Question 1   --> working with numpy

# Write a prog that makes a list, called Salaries, that has 10 ransom number between 20000 - 80000

import numpy as np

# it is a good idea to have absolute values set into variables at the beginning of your program

minSalary = 20000
maxSalary = 80000
numberOfEntries = 10

salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)    # numpy array - matrix

print (salaries)


