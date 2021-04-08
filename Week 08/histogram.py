# messing with matplotlib

# putting output to a histogram

import numpy as np 
import matplotlib.pyplot as plt 


#np.random.seed(1)    ## adding this in will keep it the same random

normData = np.random.normal(size = 100)

plt.hist(normData)
#plt.show()

plt.savefig("Firstplot5.png")  