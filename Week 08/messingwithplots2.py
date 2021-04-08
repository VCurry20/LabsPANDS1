# messing with matplotlib

# adding in label and legend

import numpy as np                  # import numpy module - use to group numbers
import matplotlib.pyplot as plt     # import matploylib in order to make the plot of the numbers

xpoints = np.array(range(1,100))    # set x axis - range from 1 - 100
ypoints = xpoints * xpoints         # set y axis - xpoints squared



# plt.plot(xpoints,ypoints)           # plot the x + y points


plt.plot(xpoints,ypoints, label = "xsquared")
plt.legend()
plt.savefig("Firstplot2.png")