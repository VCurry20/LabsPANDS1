# Lab Q2. Week 4 Flow Control if Elif and Else

# Write a Program that reads in a students percertage mark and prints out a grade
# The program should check that the percentage is valid

# Under 40% = Fail
# Between 40% - 49% = Pass
# Between 50% - 59% = Merit 2
# Between 60% - 69% = Merit 1
# Over 70% = Distinction

# Enter the percentage 67 
# Result Merit 2

percentage = float(input("enter your percentage: "))
# print ( percentage)

# becareful with ands and ors
if percentage < 0 or percentage > 100:
    print ("Please enter a number between 0 and 100")
elif percentage < 40:  # we know it is greater than 0 
    print ("Fail")
elif percentage < 50:  # between 40 - 49 
    print ("Pass")
elif percentage < 60:  # between 50 - 59
    print ("Merit 1")
elif percentage < 70:  # between 60 - 69
    print ("Merit 2")
else: # the only option left is between 70 - 100
    print ("Distinction")