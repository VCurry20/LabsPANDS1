# messing with matplotlib

# putting output to a scatterchart

import numpy as np                                                # import numpy module - use to group numbers
import matplotlib.pyplot as plt                                   # import matploylib in order to make the plot of the numbers

xpoints = np.array(range(1,101))                                  # set x axis - range from 1 - 100
ypoints = xpoints * xpoints                                       # set y axis - xpoints squared

plt.plot(xpoints, ypoints, label="sq", color="red")                            # plot line x,y label is xquard
plt.plot(xpoints, xpoints, label="straight", color="blue")        # plot line x,x lable straight, line colour blue
plt.legend()                                                      # add a legend

randompoints = np.random.randint(1, 1000, 100)                    # set random point variable with random numbers ( 1 - 1000 ( 100 of them))
plt.scatter(xpoints, randompoints, label="rand", color="yellow")                  # scatter plot, xpoints*randompoints, random label added, colour Yellow)

plt.savefig("Firstplot4.png")                                     # print out and save as 

