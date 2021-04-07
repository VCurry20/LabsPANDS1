# messing with JSON

import json                                                    # import JSON module
 
electricBill = {                                                # this is the data for the file - Dict
    'name':'Andrew',
    'amount': '999'
}

with open("storeDaata.json", "wt") as f:                       # creates file - note : "WT"              
    json.dump(electricBill, f)                                 # dumps content into the file


with open("storeDaata.json", "rt") as f:                       # opens the file "RT"
    readdict = json.load(f)                                    # sets variable for the information in JSON file
    print (readdict ["name"])                                  # print the variable but only the name listed in the dict "Andrew"


