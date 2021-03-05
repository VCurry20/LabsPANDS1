# week 5 tutorial - generate prime numbers
## TAKE 2 ##

# set up basic code
primes = []

for candidate in range (2, 101):
    #print (candidate)
    primes.append(candidate)

print (primes)

# How do we know if something is prime? It is divisable by any whole number
# Assume it is a prime
# Then do a FOR/LOOP and check if is prime >> divide number by all numbers up to that number

primes = []

for candidate in range (2, 101):
    #print (candidate)
    isPrime = True
    for divisor in range (2, candidate):
        if (candidate % divisor == 0):
            isPrime = False
            break
    
    if isPrime:
        primes.append(candidate)

print ("This is the second go", primes)
