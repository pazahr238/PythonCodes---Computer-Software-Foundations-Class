A = eval(input("enter a number: "))
count = 0

while (A != 0):
    A = A // 10
    count = count + 1

print(count)