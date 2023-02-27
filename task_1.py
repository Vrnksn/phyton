input("write a three-digit number")
# Find every digit of the number
num = int(input())
x1 = num // 100
x2 = num % 100 // 10
x3 = num % 10
print(x1, x2, x3, sep="\n")

# Find every digit is different
if x1 != x2 and x1 != x3 and x2 != x3:
    print("The digits are different")
else:
    print("The digits are not different")
    

