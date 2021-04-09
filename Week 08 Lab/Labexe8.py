# Week 8 - Lab Question 8  --> numpy / matplotlib / Plotting

# write a program that makes a list called ages that has the same values as salaries ( range 21 - 65)
# make a scatterplot of this data

# add a line to this plot the shows y = x(sq)

# copied details from Lab1 and lab7

import numpy as np
import matplotlib.pyplot as plt 


minSalary = 10000
maxSalary = 50000
numberOfEntries = 100

np.random.seed(1)          # this is so that the "random" numbers are the same each time to make it easier to debug

salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)    # numpy array - matrix

age = np.random.randint(low=21, high=65, size=numberOfEntries)         # these ( low / high ) should be set as variables at the top as opposed to like this

plt.scatter (age, salaries)               # this will be random


xpoints = np.array(range(1, 101))         # set axis values
ypoints = xpoints * xpoints               # set axis values


plt.plot(xpoints, ypoints, color='r')     # plot a line 

# plt.show()                                # show the plot - pop out

plt.savefig("plot4.png")                 # save the plot