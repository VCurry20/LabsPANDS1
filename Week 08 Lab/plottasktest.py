# Write a program that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes
# Using Matplotlib

# Methodology
# F / G / H - are x, x2, x3  / x, x*x, x*x*x ( or x^x )
# Axis = x- 0 / y = 4 - y 4 times the value  -- random?
# import modules
# add in legends / colours / etc
# show to test / fig to save when completed

import matplotlib.pyplot as plt 
import numpy as np 



xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints         # multipling each by itself - xpoints to the power of 2

plt.plot(xpoints, ypoints)
 # plt.show ()                      # show the plot / print 


plt.savefig("plot1.png")       # save the plot



# Reference 1.