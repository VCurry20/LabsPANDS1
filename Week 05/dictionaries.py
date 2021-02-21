# Lecture 5.2
# Dictionary - {}
# Distionaries - unlike lists they are not ordered - not integers
# can have dictionaries within dictionaries

# get and update function to add to a dict

# Version 1

car = {                      ### this is showing a way to list in dict - you can move the brackets and it still prints out ok 
    "make" : "ford"          ## assign a value - strs - make : ford - you need two items and :
    }

print (car)

print(type(car))  ## will be dict not ford :)

make = car ["make"]  ## if you are using [] you need to use the key from the list - the exact key "make"
print (make)    # ford

notmake = car.get ("abcdef")  ## if you tried to get a value that didnt exist it wouldnt work - but if you don't know the value is to use .get function
print (notmake)  # we are looking for "abcdef" - none will be the result
print (type(notmake))  ## type like dict or int is nonetype - it is null - not in the list




# version 2 - adding to a dict

car = {                      
    "make" : "ford",
    "price": 123 
    }         

print(car)
print(type(car))

car ["model"] = "focus"   ## this adds this to the list above
print (car)



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
print(type(car))

car ["model"] = "focus"   
print (car)

print (car ["owner"]["age"])  ## print car - owner - attribute - age / gets the age out of the owner out of the car



