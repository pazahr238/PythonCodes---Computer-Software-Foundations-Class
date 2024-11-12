import math

x1 = eval(input("enter x1: "))
y1 = eval(input("enter y1: "))

x2 = eval(input("enter x2: "))
y2 = eval(input("enter y2: "))

distance = math.sqrt((x2-x1) ** 2 + (y2-y1)**2)
print(distance)
