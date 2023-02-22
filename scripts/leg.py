# Script to find the last leg of a right triangle given two sides

import math

print("Input two sides: leave the property blank that you wish to find")

leg1 = float(input("Leg 1:      "))
leg2 = float(input("Leg 2:      "))
hypotenuse = float(input("Hypotenuse: "))

if leg1 == "":
    toFind = "leg1"
elif leg2 == "":
    toFind = "leg2"
elif hypotenuse == "":
    toFind = "hypotenuse"
else:
    print("An error occurred")

print("Finding " + toFind + ":")

if toFind == "leg1":
    print(math.sqrt((hypotenuse * hypotenuse) - (leg2 * leg2)))
elif toFind == "leg2":
    print(math.sqrt((hypotenuse * hypotenuse) - (leg1 * leg1)))
elif toFind == "hypotenuse":
    print(math.sqrt((leg1 * leg1) + (leg2 * leg2)))
else:
    print("u did something wrong and ima let u figure it out. not me.")
