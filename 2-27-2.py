A = eval(input("enter a number: "))
count = 0

for i in range(2, A):
    if (A % i == 0):
        count = count + 1

if (count == 0) and (A != 1):
    print("The number is prime")
else:
    print("The number is not prime")