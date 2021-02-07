# Monkey do from Lecture 3.1 Variables
# variable name have to start with a character - letter not a number / / case sensitive  // use camelcase


# check what type of variable this is - run python = class INT ( whole number )
age = 32
print (type(age))

# run python = class boulian - note the True needs a capital
age = True
print (type(age))

# run python = class Str (word / letter)
age = 'hello'
print (type(age))

age = "hello"
print (type(age))

###### We have not done this yet but note the following - list - tuple - dict
age = []
print (type(age))

age = ()
print (type(age))

age = {}
print (type(age))


# putting a number in to a sentence - interger into a string

# this will not work - age = 3 / print('you are ' + age)
# that will give back an error = you must convert the interger into a string as follows
age = 3
print ('you are ' +  str(age))

# convert string into an integer so when you have '3' this reads as an integer
age = '3'
print ('you are ' +  str(age))



## Very confusing part ##

# first is a dict ? - second one is a str
ageofpatient = {}
age = '3'

# here we are converting the type to a str to as can concate it to the message
print ("type of ageofpatient is :" + str(type(ageofpatient)))
print ("type of age is :" + str(type(age)))

# show how to convert a ste to an int and int to a str
print ("you are " + str(age))
nextyr = int(age) + 1
print ("next year you will be " + str(nextyr))




