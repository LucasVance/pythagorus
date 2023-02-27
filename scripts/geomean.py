# Script to find the geometric mean (altitude)
# a   x    x^2 = a * b    x = sqrt(a * b)
# - = -
# x   b

import math

num1 = input("num1: ")
num2 = input("num2: ")

print(num1 + " * " + num2 + " = " + str(float(num1) * float(num2)))
print(math.sqrt(float(num1) * float(num2)))
