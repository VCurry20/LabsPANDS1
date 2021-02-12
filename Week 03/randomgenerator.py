# program that prints out a random number between 1 - 10 

import random

number = random.randint (1,10)
print(" here is a random number {}".format(number))


# program which choose an answer from a random list of options

import random

mylist = [ "reading", "sleeping", "watching Dragrace!", "gin  and tonic", "walking", "Husband"]
answer =(random.choice(mylist))

print(" What should I do tonight?\t Answer is {}".format(answer))
