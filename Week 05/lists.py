# Week 5 - lecture one Lists and Dicts
# messing with lists
# he uses ipython on the CMD line for this but I am gonna try take most of it down here

list = [2, 3, 4, 5]
more = list + [ 2, 5, 6]

print(list)
print(more)


print (type (list))  # outputs type of list
print (len (list))   # length of list

list.append(99)  # adds to list
print(list)

# you can add to lists like you can with str or int
biggerList = list + [ 11, 12, 13]

print (biggerList)
print(list)
print (len(biggerList))  # 8

# lists can hold any variable type not just ints

aList = [ 2, 3.5, True, 'hi', {}, []]
print (len(aList))  # 6

