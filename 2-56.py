m = [] 
nr = eval(input("Enter the number of rows: "))
nc = eval(input("Enter the number of columns: "))

for i in range(0, nr): 
    m.append([]) 
    for c in range(0, nc): 
        x = eval(input("Enter an element: "))
        m[i].append(x) 

print(m) 
