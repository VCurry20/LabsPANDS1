# Week 6 Functions
# Lecture 1

# primes - script for generating primes

# This is the first way to do this - it returns both a list of the numbers and also of the prime numbers in the list of numbers
# Here you are not setting a function which can be used again
# ****** in primesFunct.py there is the same program but using functions

# there is a built in prime function so you wouldnt necessarily be writing your own code for this

primes = []
upto = 10

candidates = range(2, upto + 1)
#print(type(candidates))

for candidate in candidates:
    print(candidate, end=" ")   # print all the numbers from candidate to the end of the list - 2 -> 100 (variable upto + 1)
    isPrime = True

    # check if it is a prime
    for divisor in primes:
        if candidate % divisor == 0:  # modulus == 0 
            isPrime = False
            break

    # if it is still a prime
    if isPrime:
        primes.append(candidate) ## if it is prime add to primes =[] list


print (primes)
