# messing with matplotlib

# use the term plot not graph

import numpy as np                  # import numpy module - use to group numbers
import matplotlib.pyplot as plt     # import matploylib in order to make the plot of the numbers

xpoints = np.array(range(1,100))    # set x axis - range from 1 - 100
ypoints = xpoints * xpoints         # set y axis - xpoints squared




plt.plot(xpoints,ypoints)           # plot the x + y points

#plt.show()                            # print the plot - you need to choose this inorder to see the plot

"""## graph will pop out  with the above show option
## to save in the file use the below"""

plt.savefig("Firstplot.png")


