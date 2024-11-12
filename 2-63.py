
def fact(m):
    # Initialize F with the first term of the series
    F = 1

    # Loop through each term from 2 to n and add to F
    for j in range(2, m+1):
        F *= j

    return F

# Get input from user
n = int(input("Enter a value for n: "))

result = 1
# Call the method and display the result
for i in range(2, n+1):
    result += i / fact(i)
print(f"The result of the series for n = {n} is: {result}")