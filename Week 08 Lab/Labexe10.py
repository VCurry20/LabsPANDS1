# Week 8 - Lab Question 10  --> numpy / matplotlib / Plotting

# clean up

import numpy as np 
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberOfEntries = 100

low = 21
high = 65

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)  

age = np.random.randint(low, high, numberOfEntries)

plt.scatter(age, salaries, label='salaries')                             # add label

xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints, color='r', label='x squared')                  # add label


plt.title('random plot')    # add title
plt.xlabel('salaries')      # add name to x line
plt.ylabel('age')           # add name to y line
plt.legend()                # add legend


#plt.show()

plt.savefig("plot6.png")                 # save the plot  -- will be the same as 9