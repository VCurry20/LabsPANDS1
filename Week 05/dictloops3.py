# lecture 5.2 Dicts  
# for loops in dicts

#notes: 
# atribute is the name of the data list and the array is what is in the list

## ALSO - - to get information out of a dict use the following
# print (samplerequest ["data"]["datalist2"]["datalist3"]) = in english "from the samplerequest, go to data, then data2, and finally get data3" - what is in data 3 prints

## for keys - for x in thisdict:
##              print(thisdict[x])
# keys are the listings to the left of the : in a dict

## by keys & values - for x, y thisdict.items():     ## .items is a function
##                       print (x, y)    
# keys and values are both sides of the :



car = {
    'make' : "Fiat",   # str
    "model": "punto",
    "price": 10000,   # int
    "tags" : [ "pre-owned", "best - buy", "Dealer" ]  # array with str inside
}


print (car.items())

for key, value in car.items():
    print(key, "is on the left and this is on the right: ", value)