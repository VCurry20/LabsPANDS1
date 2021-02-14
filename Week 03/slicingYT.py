# Messing around for the task week 3 
# need to figure out how to reverse every second letter in a phrase


# need to figure out how to reverse a phrase [::-1]
# how to choose everysecond letter  // Slicing 
# delete every second letter 


# reverse a string
input = "Hello World" [::-1]
print(input)


# https://www.youtube.com/watch?v=ajrtAuDg3yw
# list explained

myList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#         0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#       -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

print(myList[5])
print(myList[-1])

# print 5 will print the 5th item on the list
# print -1 will be the last number on the list

# print group of values
print(myList[2:6])

# print to end of list - [1:9] will only print 1-8
print(myList[5:])
print(myList[:5])

# print entire list
print(myList[:])

# print a list and skip values
# starts at index 2 / going asfar as the last number -1 / 2 means every second value
# the default is to print every value so when you add in the :2 it is telling it to skip

# print numbers on my list from 4 - -1 - every second number
print(myList[4:-1:2])

# you can also reverse this process
# this will give you an emply array - you are saying here go from 4 to minus 1 (8) in twos backwards - you cannot do that
print(myList[4:-1:-2])


# you can use negative you just need to ensure there is an option for it to present data
print(myList[-1:2:-1])
# print 9 - 3

# if you want to just go from the start you can do the following
print(myList[:2:-1])
# just leave the first number blank but add the :

# you can do the same for end number if you want to include the full list
print(myList[::-1])

# or every second number in the list
print(myList[::-2])


########  LETTERS ############

# Apply the above to strings or phrases
# phrase 'I am so tired.'

samplephrase = 'I am so tired.'
print(samplephrase)

# backwards
print(samplephrase[::-1])

# how to just get "tired."" out of this sentence
# count back 6 from the end of the phrase
print(samplephrase[-6:])

# how to slice "I am" out of the sentence
print(samplephrase[4:])

# or
print(samplephrase[-10::1])

# how to remove "I am" and " tired"
print(samplephrase[4:-6])