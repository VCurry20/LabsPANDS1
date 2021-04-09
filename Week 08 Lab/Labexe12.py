# Week 8 - Lab Question 12  --> numpy / matplotlib / Plotting

# write a program that has a list of counties, make is a long list ( pick from 5)
# make some counties appear more than other
# make a pie chart

import numpy as np 
import matplotlib.pyplot as plt 

# make a list of occurances
possibleCounties = [ 'mayo','sligo','galway','leitrim','donegal']

# pick 100 randomly from possible counties whth the frequency set in p

counties = np.random.choice(
    possibleCounties,
    p=[0.1, 0.2, 0.3, 0.12, 0.28],
    size= (100)
)

# right now we need the number of occurences of each county
# this returns a tuple of the unique values and how many times they appear

unique, counts = np.unique(counties,return_counts=True)

# we can not put this into a plot
plt.bar(unique,counts)

#plt.show()

plt.savefig("plot8.png")                 # save the plot 