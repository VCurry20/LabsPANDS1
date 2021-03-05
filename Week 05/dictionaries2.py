# Lecture 5.2   --- Take 2
# Dictionary - {}
# Distionaries - unlike lists they are not ordered - not integers
# can have dictionaries within dictionaries

car = { "make" : "Ford"}

print(car)
print(type(car))

what = car["make"]  ## so when using this [] you need to make sure it exists within the list
print (what)

notmake = car.get('abcedf')  ## this is the get function
print (notmake)    ## will result in none - cannot get abcdef from the list

#aslo
print(type(notmake)) ## result will be nonetype - which means null ( could a possible use be when checking for something?)



car = { "make" : "Ford",
    "price" : "12345"}

car["model"] = "focus"

print("This is the second iteration where you have added into the list", car)



## dictionary within a dictionary

# version 3 - dict within a dict

car = {                      
    "make" : "ford",
    "price": 123,
    "owner": {
        "firstname": "fred",
        "age" : 12
    }    
    }
            
print(car)
print (car ["owner"]["age"])  ## print car - owner - attribute - age / gets the age out of the owner out of the car



