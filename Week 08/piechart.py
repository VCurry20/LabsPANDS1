# messing with matplotlib

# putting output to a piechart

import numpy as np 
import matplotlib.pyplot as plt 


#np.random.seed(1)    ## adding this in will keep it the same random

#normData = np.random.normal(size = 100)

#plt.hist(normData)
#plt.show()

fruit = np.array(["apples", "orange", "banana"])
numbers =np.array([23,54,32])

plt.pie(numbers, labels= fruit)
plt.legend()
#plt.show()

plt.savefig("Firstplot6.png")  

# pie chart only takes in numbers really - add labels to name the parts