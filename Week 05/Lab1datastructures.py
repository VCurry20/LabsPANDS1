## Lab Week 5  - Data Structures

# 1 is a quiz - retake as its tricky and good practice

# 2 Create a tuple
# create a tuple that stores the months of the yr
# from that tuple create a tuple that stores the summer months
# print out the summer months

months = ( 'january', 'febuary', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december' )
summer = months [5:8]
print(summer)


# 3 pop random numbers
# create a program that puts ten random numbers in a queue
# take one number from the queue each time and then prints the full list
# keep going until the queue is empty

import random
queue = []
numberofnumbers = 10
rangeto = 100

for n in range(0, numberofnumbers):
    queue.append(random.randint(0,rangeto))

print ("The queue is {}".format(queue))

while len(queue) !=0:
    currentnumber = queue.pop(0)
    print("current number is {} and the queue is {}".format (currentnumber, queue))

print ('The queue is now empty')




# 4 courses 
# Write a program that stores a student's name and a list of her courses and grades in a dict
# The program should then print out her data
# The numbers of courses could change - is a variable

student = { 
    "name" : "Mary",
    "modules" : [ 
        {
            "coursename" : "programming",
            "grade" : 45
        },
        {
            "coursename" : "History",
            "grade":"99"
        }
    ]
}

print ("This student is: {}".format(student["name"]))

for module in student ["modules"]:
    print("\t {} \t: {}".format(module["coursename"], module["grade"]))





