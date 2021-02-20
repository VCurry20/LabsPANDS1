# lab 4.2
# Write a program that prompts the user to guess a number
# the prgram should keep prompting until the user guess the right number

## Should look like this
# PLease guess a number: 2
# Wrong
# PLease guess again: 5
# Wrong
# PLease guess again: 30
# Well done! Yes the number was 30 

numbertoguess = 30

guess = int (input("Please guess a number:"))
while guess != numbertoguess:
    print ("Wrong!")
    guess = int(input("Please guess again:"))

print ("Well done! Yes the numbers was ", numbertoguess)
