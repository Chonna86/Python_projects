first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))
if first < second :
    gcd = first
else :
    gcd = second
    
while float(first % gcd != 0) or float(second % gcd != 0) :
    gcd -= 1
print(gcd)

def func() :
    pass