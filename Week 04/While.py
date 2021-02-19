# Lecture 4.2 While 
# Monkey See Monkey Do from Lecture

# Whlie Conditions:
#       Statements indent


# COUNTER CONTROLLED LOOP
# you set the parameters and it keeps going until it reaches the parameters
# Count = 0, while count is less than 10 print count, numbers in incredments of 1
count = 0
while count < 10 :
    print (count)
    count += 1


print ( "Example 2")

count = 10   # state @ 10
while count >= 0:  # while count is greater or = 0
    print (count)
    count -= 1  # go in reverse  ( note the minus )
print ("Blast OFF") # after this has been completed blast off is the next thing executed




# SENTINAL CONTROLLED LOOP 

# input always returns a string 
# for this while loop it will keep going until you enter a value - which you have set. its an continual loop

val = input (" enter something ( q to quit ): ")
while val != 'q' :
    print ("you said: " + val) # do something
    val = input ("(q to quit)")
print ( "Goodbye")
