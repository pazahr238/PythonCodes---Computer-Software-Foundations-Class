tuition = new_tuition = 10000
count = 0

while (tuition * 2 > new_tuition):
    new_tuition = new_tuition * 1.07
    count = count + 1

#print("The new tuition is = ", new_tuition)
print("The count is = ",  count)
