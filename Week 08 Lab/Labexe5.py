# Week 8 - Lab Question 5  --> numpy / matplotlib / Plotting

# write a program that plots function y = x -power of 2

import matplotlib.pyplot as plt 
import numpy as np 

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints         # multipling each by itself - xpoints to the power of 2

plt.plot(xpoints, ypoints)
 # plt.show ()                      # show the plot / print 


plt.savefig("plot1.png")       # save the plot