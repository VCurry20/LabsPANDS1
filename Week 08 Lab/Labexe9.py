# Week 8 - Lab Question 9  --> numpy / matplotlib / Plotting

# amend lab8 - 
# add a legend, titles and axix labels to the plot

import numpy as np 
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberOfEntries = 100

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint(low=21,high=65, size=numberOfEntries)

plt.scatter(ages, salaries, label='salaries')                             # add label

xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints, color='r', label='x squared')                  # add label


plt.title('random plot')    # add title
plt.xlabel('salaries')      # add name to x line
plt.ylabel('age')           # add name to y line
plt.legend()                # add legend


# plt.show()

plt.savefig("plot5.png")                 # save the plot