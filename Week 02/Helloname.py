# program uses a variable to greet
# Author Veronica Curry

name = "Andrew"
print (' hello '  + name)

#solutions for when variable is an number 
age = 34
# print ('your age is ' + age ) this will not work as it cannot just be an interger

#using str function is one solution
print('your age is ' + str(age))

# print ('your age is ' + age ) using format function is another solution
print ( 'your age is {}' .format(age))

# if you have two variables in one sentence it is structured as follows 
print('hello {} your age is {}'.format(name,age))

