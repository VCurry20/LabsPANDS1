# lab 4.2
# modify the program in guess1.py

# Write a program that prompts the user to guess a number
# the prgram should keep prompting until the user guess the right number

## Also add in that the users guess was too high or too low 

## Should look like this
# PLease guess a number: 22
# Too Low  ## - instead of just " Wrong "
# PLease guess again:  55
# Too High
# PLease guess again: 30
# Well done! Yes the number was 30 


numbertoguess = 30

guess = int (input("Please guess a number:"))
while guess != numbertoguess:
    if guess < numbertoguess:
        print ("Too Low")
    else: print ("Too High")
    guess = int(input("Please guess again:"))

print ("Well done! Yes the numbers was ", numbertoguess)




#### EXTRA #####

## GET THE PROGRAM TO GENERATE A RANDOM NUMBER BETWEEN 0 - 100 TO GUESS

# Random number generator -

import random

numbertoguess = random.randint (0,100)

print ( "The random number to guess is ", numbertoguess)

guess = int (input("Please guess a number:"))
while guess != numbertoguess:
    if guess < numbertoguess:
        print ("Too Low")
    else: print ("Too High")
    guess = int(input("Please guess again:"))

print ("Well done! Yes the numbers was ", numbertoguess)