# Lab Week 7 - 2 C

# Combine both A + B - write a program that will count how many times a program has been run. 
# Test it to check the number increases each time.

filename = "count.txt"

def readNumber ():
    with open (filename) as f:
        number = int(f.read())
        return number


def writeNumber (number):
    with open (filename, "wt") as f:
        #write takes a string so we need to convert
        f.write (str(number))

# main

num = readNumber()
num +=  1

print ("we have run this program {} times".format(num))
writeNumber(num)
