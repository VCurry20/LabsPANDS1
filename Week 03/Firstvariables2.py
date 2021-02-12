# Monkey see monkey do from Wk 3 -- This is a re-do
# Week 3 - Variables 
# Veronica Curry

# here you assign a variable and it will assess it but you need it to tell you 
age = 32
type(age)

# print function will now tell you what type is age = 32 - interger
age  = 32
print (type(age))

# Types of Variable
# Age equals true - boolean present one of two values- true or false
age = True
print (type(age))

# Age equals a String - single and then double quotes
age = 'Hello'
print (type(age))

age = "Hello"
print (type(age))

# Age is equal to a list
age = []
print (type(age))

# Age is equal to a Tuples
age = ()
print (type(age))

# Age is equal to a Dict
age = {}
print (type(age))

# String
# ageofpatient = {}
# age = 3
#print (type(ageofpatient))
#print (type(ageofpatient))

# print ("you are a" + age)
# this will not work because are trying to add an integer to a string - a number to a list of letters / can only concat str (not int) to str

# Solution: - convert intr to str - 
ageofpatient = {}
age = 3
print (type(ageofpatient))
print (type(ageofpatient))

print ("you are " + str(age))

# if you had listed age = '3'  = this would be stored as a string not an int


# messing around with type and printing type of
ageofpatient = {}
age = '3'
print ("type of ageofpatient is :" + str(type(ageofpatient)))
print ("type of age is:" + str(type(age)))

print ("you are " + str(age))

# use varient values to form sentences // need to add str on front of values that are integers if we are using the values as strs
ageofpatient = {}
age = '34'
print ("type of ageofpatient is :" + str(type(ageofpatient)))
print ("type of age is:" + str(type(age)))

print ("you are " + str(age))
nextyr = int(age) + 1
print ("next yr you will be " + str(nextyr))

# with notes breakdown

#variant assigned
ageofpatient = {}
age = '34'

# print type of varient - also change int to str  // need to conver int to str so we can concate it to the str message // could also use Format
print ("type of ageofpatient is :" + str(type(ageofpatient)))
print ("type of age is:" + str(type(age)))

print ("you are " + str(age))
nextyr = int(age) + 1
print ("next yr you will be " + str(nextyr))