# lecture 5.2 Dicts
# for loops in dicts

car = {
    "make" : "Fiat",   # str
    "model": "punto",
    "price": 10000,   # int
    "tags" : [ "pre-owned", "best - buy", "Dealer" ]  # array with str inside
}

# print(car)

for key in car:   ## prints out just the keys 
    print(key)

for key in car:
    print(key, "have a value", car [key])  ## prints out keys in a sentence eg make 'have a value' fiat


print ( car . items())  # built in functions  **** review functions

for pair in car.items():
    print(pair)
    print(type(pair))


print ( car . items())  # becuase its a tuple you can use value    ***** review this
for key,value in car.items():
    print (key, "have a value", car [key])


print ( car . items())  # becuase its a tuple you can use value
for key,value in car.items():
    print (key, "have a value", value)
