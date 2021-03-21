# Write a program that takes a positive floating-point number as input and outputs an approximation of its square root
# You should create your own function

# Week 6
# Task 6

# Veronica Curry
# Student ID: G00074924

# The numbers should look like this:
# Please enter a positive number: 14.5
# The square root of 14.5 is approx. 3.8


# Research Methodology:
# What is a Sq Root and how do we work it out?
# Sq Root in Python and how it operates
# 
# 


def squareRoot (n):                 # 1.
    x= float(n)                     # 2.
    y=1.000000                      # 3. iteration initialisation.
    e=0.000001                      # 4. accuracy after decimal place.
    while x-y > e:                  # 5.
        x= (x+y)/2                  # 6.
        y= n/x                      # 7.
    print (round(x,2))              # 8.

n = input('enter the number : ')    # 9.
squareRoot (float(n))               # 10.


# Reference 1: https://www.youtube.com/watch?v=PJHtqMjrStk
# Reference 2: https://realpython.com/python-square-root-function/
# Reference 3: https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/#:~:text=Let%20N%20be%20any%20number,correct%20square%20root%20of%20N.
# Reference 4: https://stackoverflow.com/questions/46183020/square-root-without-pre-defined-function-in-python
# Reference 5: https://surajregmi.medium.com/how-to-calculate-the-square-root-of-a-number-newton-raphson-method-f8007714f64
# Reference x: https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points