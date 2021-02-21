# 5.1 lecture 
# Tuples

# use () brackets
# look like lists
# cannot be changed - immutable
# can unpack tuples

tupleexample = (1, 2, 3)

# can get len
print (len (tupleexample))

# can get a certain character - again its 0,1,2,3 etc not 1,2,3 etc
print(tupleexample[1])

# you cannot however do the following and amend the () tuple
# tupleexample[2] = 99

# also you cannot append to a  () tuple
# tupleexample.append(99)  # WIIL NOT WORK WITH TUPLE
# print(tupleexample)


# What you can do however is take that data from a tuple and assign muliple variables from the data within the tuple

tupledata = (11, 12, 13, 14)
a, b, c, d = tupledata

print (a)
print (d)
