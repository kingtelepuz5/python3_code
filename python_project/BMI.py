#your code goes here
print('Hi it\'s program value you BMI')
print('Pls input you weight')
weight = float(input())
print('Pls input height')
height = float(input())

bmi = (weight/(height**2))
a = bmi
if a < 18.5:
   print('Underweight')
elif 18.5 <= a <= 25.0:
   print('Normal')
elif  25.0 >= a or a < 30.0:
   print('Overweight')
else:
   print('Obesity')

print('it\'s you BMI:', a)
