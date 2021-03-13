name = input ('Enter your name: ')
print('Hello ' + name + '\nNice to meet you, lets calculate your BMI!')

height = float(input('Enter your height in CM: '))
heightinmeters = height / 100

print('Your height in meters is {}'.format(heightinmeters))

weight = float(input("Input your weight in Kilogram: "))

print('Your weight is {}'.format(weight))

BMI = (round(weight / (heightinmeters * heightinmeters), 2))
print ( " Your BMI is {}".format (BMI))



# details given by Andrew - weight 65kg / height 180cm / formula w/h**  - Result - 20.06