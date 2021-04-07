# Lab Week 7 - 2 B

# write to a program = writes the number into the count.txt file - over writes - not append
# run this file - ck the count.txt before and after to confirm change

filename = "count.txt"
def writeNumber (number):
    with open(filename, "wt") as f:
        # write takes a string so we need to convert
        f.write(str(number))

# test it
writeNumber(4)