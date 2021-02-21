# lecture 5.1 - breaking down and messing with forloop
# take 2 - prints out each element of a list with its number listing = 4 element is 6

list = [2, 4, 5, 6]
more = list + [2, 5, 6]

print (more)



list = [2, 4, 5, 6]
more = list + [2, 5, 6]

for key in range (0,len(more)):  ## sets the range of key
    print ( " bla bal bal [",key, "] = ", more [ key ])  ## more element 0 is equal to the value of 0

##               [0, key, 0]  --> so its saying start at 0 - up to key - 0 means positive
##                                    [value of key]


list = [2, 4, 5, 6]
more = list + [2, 5, 6]

for key in range (0,len(more)):  ## sets the range of key
    print ( " bla bal bal [",key, "] = ", more [ key ])  ## more element 0 is equal to the value of 0