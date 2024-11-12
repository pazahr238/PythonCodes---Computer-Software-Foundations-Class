A = eval(input("Enter numebr A : "))
B = eval(input("Enter numebr B : "))


try:
    C = A / B
    print(C)
except:
    print("You encountered an error division by zero")

