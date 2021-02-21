# week 5 tutorial - generate prime numbers

# advise - before you start writing code - write out what you need to do and break it down in steps - then write code

# the purpose of this  code is to:
# Test of the numbers between 2 - 100 are prime
# prime numbers are no divisible by other numbers / integers
# program will tesst the numbers range 2 - 100 to see if they can be divided

# test 
for candidate in range (2, 101):  ## give full names for variables  - go ck 100 - range needs to go to 101
    print ( candidate )



# version 1 - set up list
primes = [] # list for candidates as we find them


for candidate in range (2, 101):  ## give full names for variables  - go ck 100 - range needs to go to 101 - this will be tidied up later - this is hardcoded currently
   # print ( candidate )
   primes.append(candidate)  # puts the numbers in the primes list - no changes have yet been made to the range - all numbers still included

print (primes)  ## print out - to check its working



# version 2 - find prime numbers - ck if numbers are divisible by another whole number

primes = [] 

for candidate in range (2, 101):  
   # print ( candidate )
   isPrime = True  # assumes numbers are prime - sets boolean 
   for divisor in range (2, candidate): # forloop - going to see if for each of the numbers from 2 up wards, if they are divisible into the number
       if (candidate % divisor == 0):  # if candidate number divided by divisor is % = 0 then it is false
           isPrime = False
           break # ends cycle - jumps out of foreloop after it checks if prime

   if isPrime:
        primes.append(candidate)

print (primes)


# go through all the candidates from 2 - 100
# assume it is a prime
# check all the divisors from 2 - up to the candidate value ( for two just check 2/2 - for three 3/2 3/3 - for four 4/2 4/3 4/4 etc)
# if candidate % divisor is not equal to 0 it is a prime 
# isprime as it is no ==0
# jump out of foreloop


# version 3 - tidy code - remove hard coding of numbers

# As the number we are checking gets higher (variable - upto) it will take the comp longer to run the code - if we tidy it up it will run quicker.
# a program taking time to run = program too long? needs tidying?

# in version 2 the code was checking every number in the range to see if it was divisible by the range basically
# we don't need to check if its divisible by every number-  we can check by only the prime numbers


primes = [] 

upto =  100000   # set a varient 
for candidate in range (2, upto):  
   # print ( candidate )
   isPrime = True
   for divisor in primes:    # only need to check if divisible by prime numbers
       if (candidate % divisor == 0):   # if divisible by an int it is not a prime number
           isPrime = False
           break # so there is no reason to keep checking 

   if isPrime:
        primes.append(candidate)

print (primes)



## there is even more ways to make this more compact
### this just shows the forloops and list
#### this is not simple code 
##### add comments to all code
###### add varibles - not hard numbers for the top values