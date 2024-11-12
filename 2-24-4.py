A = eval(input("enter a number: "))
ReversedA = 0

while (A != 0):
    C = A % 10
    ReversedA = (ReversedA * 10) + C
    A = A // 10

print(ReversedA)