# Going through the exercise in each Chapter of A Whilewind Guide to Python
# These are the exercies from the Variables and Objects

# going through the examples in the text

# Changing the assigned value - when that value is assinged to two varients - changes the value for both
# .append - means add to / function of python
x = [ 1, 2, 3, 4]
y = x
print (y)

# Now amend x
x.append(5) 
print (y)


# also note that if we change the value of x in this scenario the value of y is unchanged
x = 10 
y = x

x += 5

print("x = ", x )
print("y = ", y)


## Objects

## real and imaginary value in a complex number ((NO CLUE WHAT THE MEANS))

x = 4.5
print(x.real, "+", x.imag, "i")

