# Week 6 Functions
# Lecture 1
# primes - script for generating primes using a function
# this is the follow on program from primes.py
# this does not easily amend from primes.py 


import math
primes = []   # list which we will print at then end  # this is a global variable
upto = 10     # variable which can be amended


## this part is setting the function 
## when creating a function is should be self contained - not be dependant on outside variables

def isPrime(candidate):  ## what am I putting in
    # check if it is a prime
    for divisor in range (2, math.floor(math.sqrt(candidate))):  ## math equation to look for the Sq root as opposed to using
        if candidate % divisor == 0:
            return False
    return True    ## I want it to return a boolean


## this is using the function
candidates = range (2, upto + 1)
#print (type(candidates))
for candidate in candidates:
    # if it is still a prime:
    if isPrime(candidate):
        primes.append(candidate)

    
print (primes)

## The main point to take from this is how to think about writing code 
## Functions should make your programs simplier and more compact

