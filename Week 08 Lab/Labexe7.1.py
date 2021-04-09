"""" messing with the variables in lab7 """


# Week 8 - Lab Question 7  --> numpy / matplotlib / Plotting

# write a program that makes a list called ages that has the same values as salaries ( range 21 - 65)
# make a scatterplot of this data

# copied details from labexe1.py

import numpy as np
import matplotlib.pyplot as plt 

minSalary = 20000
maxSalary = 80000
numberOfEntries = 100

lowno = 21
highno = 65

np.random.seed(1)          # this is so that the "random" numbers are the same each time to make it easier to debug

salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)    # numpy array - matrix

# age = np.random.randint(low=21, high=65, size=numberOfEntries)         # these ( low / high ) should be set as variables at the top as opposed to like this
age = np.random.randint(lowno, highno, numberOfEntries )

plt.scatter (age, salaries)      # this will be random

plt.show()                       # show the plot - pop out

# plt.savefig("plot3.png")       # save the plot
