# Lab Week 7 - 2 A

#Print the number from the file - str to int

filename = "count.txt"
def readNumber():
    with open(filename) as f:
        number = int(f.read())
        return number

## test it
num = readNumber()
print (num)
