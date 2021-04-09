# Week 8 - Lab Question 6  --> numpy / matplotlib / Plotting

# Write a prog that plots a histogram of the salaries as listed in Labexe1

# copied details from labexe1.py

import numpy as np
import matplotlib.pyplot as plt 

minSalary = 20000
maxSalary = 80000
numberOfEntries = 100

np.random.seed(1)          # this is so that the "random" numbers are the same each time to make it easier to debug

salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)    # numpy array - matrix

plt.hist(salaries)

# plt.show()                  # show the plot - pop out

plt.savefig("plot2.png")       # save the plot

