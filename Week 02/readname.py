# read in a name and print it out
# Author Veronica Curry
# note I have repeated phrases to show progression so you when you run the code the sentences to appear multiple times 

#this is a basic line and achieves very little
input('enter your name:')

# you need variable from which you can add more commands
name = input('enter your name:')

#greet and name
print('Hello ' + name)

#age
input('what is your age?')

#age plus variable to make more of a proper conversation
age = input('What is your age')
print('Your age is ' + age)

# age plus name 
print ('Your name is {}, and your age is{}'.format(name, age))