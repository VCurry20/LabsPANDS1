# Week 5 - lecture 1 - lists & dicts
# indexing and slicing in lists
# using forloops with list

# take out various elements of a list - iterating through a list

list = [2, 4, 5, 6]
more = list + [2, 5, 6]

for x in more:
    print( 'Getting back at the study', x)


## Using Range

for y in range (0,10):
    print (y)

for x in range ( 22, 30):
    print(x + 1)

for q in range (0,len(more)):
    print ('this is the middle option', q)

for key in range (0,len(more)):
    print ("this[",key,"] =", more)

for key in range (0,len(more)):
    print ("this is the second time [",key,"] =", more[key])

print (more)