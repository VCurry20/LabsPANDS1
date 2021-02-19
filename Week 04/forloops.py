# Lecture 4.2 While loops 
# Monkey See Monkey Do from Lecture

# for elem in list:  (iterting through a list)
        # do something


# give lists a plural name
boats = [ 'sigma', 'beneteau', 'swan']

for boat in boats:
    print ( " i'd prefer to be out on a " + boat)


# if one of the items in the list was a number - 
boats = [ 'sigma', 'beneteau', '99']

for boat in boats:
    print ( " i'd prefer to be out on a " + str (boat))

# indentation matters for these - 

boats = [ 'sigma', 'beneteau', '99']

for boat in boats:
    print ( " i'd prefer to be out on a " + str (boat))
    print ( " Sailing on the sea") ## move this in and it will come out of the loop - it will only print once


# for number in range ( 1, 10)
        # do something


for number in range (1, 11):
    print ("hello", number)


