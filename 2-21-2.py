p = 0
n = 0
i = 0
N = eval(input("enter the number of values : "))

for indx in range(N):
        A = eval(input("enter a number : "))
        if (A > 0):
            p = p + 1
        if (A == 0):
            n = n + 1
        if (A < 0):
            i = i + 1

print(p, n, i)


