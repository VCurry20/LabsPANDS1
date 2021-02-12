# extras on Lab 3.2 Fun with Numbers
# convert.py
# input -9.44 Dollars - output in cents

# Write a program that takes in a float amount in dollars and returns an absolute amount in cents

# Please enter - 5.99
# The amount in cent is 599

# use rounding first and then convert

dollars = float(input(" How many dollars have you: "))
absoluteDollars = abs(dollars)
cents = (absoluteDollars * 100)
intcents = int(cents)
print(" You have {} dollars which is {} in cent".format(absoluteDollars, intcents))