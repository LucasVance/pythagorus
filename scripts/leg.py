# Script to find the last leg of a right triangle given two sides

import math

print("Input two sides: leave the property blank that you wish to find")

leg1 = input("Leg 1:      ")
leg2 = input("Leg 2:      ")
hypotenuse = input("Hypotenuse: ")

if leg1 == "":
    toFind = "leg1"
elif leg2 == "":
    toFind = "leg2"
elif hypotenuse == "":
    toFind = "hypotenuse"
else:
    print("An error ocurred")

print("Finding " + toFind + ":")

if toFind == "leg1":
    print(math.sqrt((float(hypotenuse) * float(hypotenuse)) - (float(leg2) * float(leg2))))
elif toFind == "leg2":
    print(math.sqrt((float(hypotenuse) * float(hypotenuse)) - (float(leg1) * float(leg1))))
elif toFind == "hypotenuse":
    print(math.sqrt((float(leg1) * float(leg1)) + (float(leg2) * float(leg2))))
else:
    print("u did something wrong and ima let u figure it out. not me.")
