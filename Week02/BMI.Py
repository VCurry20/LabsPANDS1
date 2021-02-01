# Calculate BMI from a persons weight and height
# Veronica Curry

# for reference - BMI formula http://www.kingsweightlossclinics.co.uk/resources/bmi-checker/
# for reference - BMI Python https://stackoverflow.com/questions/20405610/bmi-calculator-in-python/50386292#:~:text=')%20while%20input%20%3D%3D%20'imperial,which%20means%20you%20are%20underweight.

name = input (' What is your name?')
print('Hello ' + name )
print('Today we will calculate your BMI')
print('What is your weight in kilos?')
weight = int(input('What is your weight in kilos?'))
print('What is your height in CM?')
height = int(input('What is your height in CM?'))
print(heightinmeters = height / 100)
print(BMI = weight / (heightinmeters**2))