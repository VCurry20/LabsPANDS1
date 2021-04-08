# messing with matplotlib

# adding in an additional line

import numpy as np                  # import numpy module - use to group numbers
import matplotlib.pyplot as plt     # import matploylib in order to make the plot of the numbers

xpoints = np.array(range(1,100))    # set x axis - range from 1 - 100
ypoints = xpoints * xpoints         # set y axis - xpoints squared



plt.plot(xpoints,ypoints)           # plot the x + y points

plt.plot(xpoints,ypoints, label = "xsquared")                          # plot line x,y label is xquard
plt.plot(xpoints, xpoints, label = "Straight", color= "blue" )         # plot line x,x lable straight, line colour blue
plt.legend()                                                           # add a legend
plt.savefig("Firstplot3.png")                                          # print out and save as 



### When this prints you will see that the second long is straight - you need to check the x and y points prior to starting a plot to see what is useful for you / scales on the axis

