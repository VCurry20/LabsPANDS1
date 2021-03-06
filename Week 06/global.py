# Week 6 lecture 2
# Syntax


# variable scope
## All of the parts under def are within the scope of that variable (liek the if statements they are within the if 'tree'/ indentation)


var = 10

def cube (num): 
    global var        
    var = 66   
    print ("This is the variable in the function", var)       
    return num ** 3    

cube(2)
print ("This is the variable outside the function", var)             

 
## you need cube(22) to get it to print




#### THIS GLOBAL VARIANT SETS TOO VAR'S TO BE 66 ####
'THIS IS BECAUSE YOU ARE TELLING THE FUNCTION THAT YOU WANT TO USE THE GLOBAL VARIENT NOT THE LOCALE'
'THE LOCAL VARIENT IS WITHIN THE FUNCTION THE GLOBAL IS AT THE TOP OF THE PROGRAM OR OUTSIDE OF THE FUNCTION'
'THIS IS NOT RECOMMEND TO USE - MORE TO KNOW THE POSSIBLE ERRORS FROM IT'