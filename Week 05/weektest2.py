import datetime

weekDays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
 
def whichDay (weekday):
    
    for weekDays in range (0,4):
        return ("Yes, unfortunately it's a weekday")

    else:
        return ("It is the weekend, yay!")


day = input ("Please enter a day of the week: ")  
print (whichDay (day))