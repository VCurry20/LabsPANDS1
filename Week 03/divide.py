# write a program that reads in two numbers and divides the first by the second = giving the integer and the remainder
# Therefore give the result in a number whole and a division remainder %

x = int(input (" Enter your first number: "))
y = int( input(" Enter the number you want to divide by: "))

# // gives you the int division
Answer = int(x/y)

# % gives the remainder
Remainder = x%y

# print the answers out
print(" {} divided by {} is {} with remainder {}".format(x, y, Answer, Remainder))
