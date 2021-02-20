# Week 5 - lecture 1 - lists & dicts
# indexing and slicing in lists
# he uses ipython on the CMD line for this but I am gonna try take most of it down here

# this is how you get information out of a list - individual items

# indexing for single items
# slicing for multiple items

# Note: Computer languages start a 0 not one
# the first item in a [] are numbered as 0
# [ a, b, c, d] = 0, 1, 2, 3


aList = [ 2, 3.5, True, 'hi', {}, []]

print(aList[0])  #2
print(aList[2])  #true
# there is no alist[6] - there is only 0 - 5

# to get the last element in a list - all of these work the same way
print(aList[6 - 1])  
print(aList[5])
print(aList[len(aList)-1]) 
print(aList[-1])

# you can also change one element in the list without amending the rest
aList[4] = 99
print(aList)


# Slicing information out of the list
print(aList [1 :4])  # element 1 - 4
print(aList [:4])    # element beginning of list 0 - 4
print(aList [1 :])   # element 1 - end of list

print(aList [::2])  # every second - from the beginning to the end - jump 2
print(aList [::-1]) # reverses the list - from beginning to the end - power of minus 1- negative one




