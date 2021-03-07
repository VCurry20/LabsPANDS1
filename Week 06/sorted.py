# Week 6
# Lecture 3

# this is as an FYI and I need to go over the further reading for this to make sense
# need to watch the video with this as you need to mess with the code and see what happens in progression
# follow on from lambda.py

#sorted
# this is will put numbers in proper order
list = [22, 20, 24, 23, 21]
print (list)

newlist = sorted(list)
print(newlist)




# Sorting dictionary 
# when sorting dictionary lists we need to use functions

data = [ {'first': 'Veronica', 'last' : 'Curry', 'YOB' : 1984},
         {'first': 'Paul', 'last' : 'ODriscoll', 'YOB' : 1983},
         {'first': 'George', 'last' : 'DOC', 'YOB' : 2020}]


def sortfun (item):
    return item ['first']   ## telling it to sort by first name

print (data)
newdata = sorted(data, key = sortfun) #sort using sortfun function
print (newdata)


# a tidier way to get it to print is as follows
newdata = sorted(data, key = sortfun) #sort using sortfun function
for item in newdata:
    print (item)


# using lambda
newdata = sorted (data, key = lambda item : item ['last'])
for item in newdata:
    print('This is the last list', item)



