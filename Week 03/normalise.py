# This program reads in a string and strips including any leading or trailing spaces
# It also converts all the letters to lower case
# This program also outputs the length of the original string and also the normalised one

# set variables
rawstring = input( "Please enter a string of text: ")
normalisedString = rawstring.strip().lower()

lengthofrawstring = len(rawstring)
lengthofnormalised = len(normalisedString)

# out put sentences

print("That string normalised is: {}".format(normalisedString))
print("We reduced the string input from {} to {} characters".format(lengthofrawstring, lengthofnormalised))
