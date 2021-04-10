# Week 8 - Lab Question Extra

# Add a line of normal distribution to the plot in lab9 - using seaborn

import numpy as np 
import matplotlib.pyplot as plt

import seaborn as sns                                                   # adding seaborn

minSalary = 20000
maxSalary = 80000
numberOfEntries = 100

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint(low=21,high=65, size=numberOfEntries)

plt.scatter(ages, salaries, label='salaries')                            

xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints, color='r', label='x squared')                  


plt.title('random plot')    
plt.xlabel('salaries')      
plt.ylabel('age')           
plt.legend()                


plt.show()

# plt.savefig("plot9.png")                 