# Find if a triangle is a right, acute, or obtuse triangle, given lengths of 3 sides

leg1 = float(input("Leg 1:      "))
leg2 = float(input("Leg 2:      "))
hypotenuse = float(input("Hypotenuse: "))

if ((leg1 * leg1) + (leg2 * leg2) == hypotenuse * hypotenuse):
    print("Right triangle")
elif ((leg1 * leg1) + (leg2 * leg2) > hypotenuse * hypotenuse):
    print("Acute triangle")
elif ((leg1 * leg1) + (leg2 * leg2) < hypotenuse * hypotenuse):
    print("Obtuse triangle")
else:
    print("An error occurred")