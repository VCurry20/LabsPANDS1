# Week 5 - lecture 1 - lists & dicts
# indexing and slicing in lists
# using forloops with list

# take out various elements of a list - iterating through a list

list = [2, 4, 5, 6]
more = list + [2, 5, 6]

print (more)


# print out each element individually
list = [2, 4, 5, 6]
more = list + [2, 5, 6]

for x in more:
    print ("element in list: ", x)   ## for each number listed in "more" print out "element in list:" + number


# using range

list = [2, 4, 5, 6]
more = list + [2, 5, 6]

for x in more:
    print ("element in list: ", x)

for key in range (0, len(more)):  ## prints out the len of the range of the list -> 0-6 (7 items)
    print (key)


# take 2 - prints out each element of a list with its number listing = 4 element is 6

list = [2, 4, 5, 6]
more = list + [2, 5, 6]

for key in range (0,len(more)):  ## sets the range of key
    print ( " more[",key, "] = ", more [ key ])  ## more element 0 is equal to the value of 0
 ##               [0, key, 0]  --> so its saying start at 0 - up to key - 0 means positive
 ##                                    [value of key]
