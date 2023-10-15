num = int(input("Enter integer (0 for output): "))
sum = 0
while int(num) :
    i = 0
    for i in range(num + 1) :
        sum = sum + i
        i += 1
        
    num = int(input("Enter integer (0 for output): "))
print(sum)

