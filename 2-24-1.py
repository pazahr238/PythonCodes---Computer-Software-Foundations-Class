a = eval(input("enter a :"))
b = eval(input("enter b :"))

c = a % b
while (c != 0):
    a = b
    b = c
    c = a % b

print(b)



