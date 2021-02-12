# Lab 3.2 Fun With Numbers
# Rounding 

# Programs takes in a float and outputs an rounded number ( rounded up or down accordingly)
# Enter float -5.99
# 5.99 rounded is 6

# Notes:
# Becareful of round function - it rounds to the nearest even number
# eg 4.5 rounds to 4, 5.5 rounds to 6
# Not to be used where accuracy is essential

numberToRound = float(input( "enter a float number:"))
roundedNumber = round(numberToRound)
print('{} rounded is {}'.format(numberToRound, roundedNumber))
