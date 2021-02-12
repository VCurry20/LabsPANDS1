# labs 3.2 Fun with Numbers
# Floor function - takes in a float returns an int rounded down
# You will need the math module math.floor()

# enter a float number - -5.99
# 5.99 floored is 5

import math

numberTofloor = float(input("Enter a float number: "))
flooredNumber = math.floor(numberTofloor)
print("{} floored is {}".format(numberTofloor, flooredNumber))