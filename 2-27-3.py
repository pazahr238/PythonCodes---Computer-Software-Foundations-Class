N = eval(input("How many numbers: "))
sum = 0

for i in range(1, N+1):
    A = eval(input("enter a number: "))
    sum = sum + A

avg = sum / N
print(avg)