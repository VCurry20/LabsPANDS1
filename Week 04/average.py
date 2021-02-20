# Labs 4.2
# For Loops

# Write a program that keeps reading numbers until the user enters 0 ( the program should append each into a list)
# The program should print out each of the numbers enetered and the average of them ( use a list)

# enter a number ( 0 to quit): 33
# enter another ( 0 to quit): 34
# enter another ( 0 to quit): 0
# 33
# 34
# The average is 33.5


# Answer

# This program read in numbers until 
# The user enters 0
# it will then print them back
# and their average

numbers = []   # list is plural

# first number then we check if it is 0 in the while loop
number = int(input("Enter number (0 to quit):"))

while number != 0:
    numbers.append(number)

    # read the next number and check if 0
    number = int(input("Enter another (0 to quit):"))

for value in numbers:
    print (value)

# I want average to be a float

average = float(sum(numbers)) / len(numbers)
print ("The average is {}".format(average))
