# messing with Numpy

# with numpy you cannot have a mix or str, int and float it can only be all of the same


import numpy as np 


listOfNumber = [1,2,3,4,6]         # this is just a normal list
print(listOfNumber)                # this will print out the list of number - note the commas will print in this case


numbers = np.array([1,2,3,4,5])    # this is an array in numpy
print(numbers)                     # this will print out the numpy array - note no commas will print out


# Adding  / multiplying

""" listOfNumber = listOfNumber + 3 """   # this will not work - you cannot add to a list like this

# in numpy
numbers = numbers + 3   # this will work and will add 3 to all the numbers inside as this information is held in a maxtrix
print (numbers)         # this will also work for * 


# You can also multiply numpy arrays by numpy arrays

numbers = numbers * np.array([1,2,3,4,5])   # matrix by matrix < 1*1,2*2,3*3,4*4,5*5 > also the same amount of numbers must be in both maxrix
print (numbers)



# Random generator

randomNumbers = np.random.randint(100,200,5)  # pick 5 random numbers between 100 - 200 and add them to a numpy array
print (randomNumbers)



