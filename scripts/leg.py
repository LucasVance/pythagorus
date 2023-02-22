# Script to find the last leg of a right triangle given two sides

import math

print("Input two sides: leave the property blank that you wish to find")

leg1 = float(input("Leg 1:      "))
leg2 = float(input("Leg 2:      "))
hypotenuse = float(input("Hypotenuse: "))

if leg1 == "":
    to_find = "leg1"
elif leg2 == "":
    to_find = "leg2"
elif hypotenuse == "":
    to_find = "hypotenuse"
else:
    print("An error occurred")

print("Finding " + to_find + ":")

if to_find == "leg1":
    print(math.sqrt((hypotenuse * hypotenuse) - (leg2 * leg2)))
elif to_find == "leg2":
    print(math.sqrt((hypotenuse * hypotenuse) - (leg1 * leg1)))
elif to_find == "hypotenuse":
    print(math.sqrt((leg1 * leg1) + (leg2 * leg2)))
else:
    print("u did something wrong and ima let u figure it out. not me.")
