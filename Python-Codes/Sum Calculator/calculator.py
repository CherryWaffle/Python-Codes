sum1 = sum2 = 0

num1 = int(input("Enter number one : "))
num2 = int(input("Enter number two : "))
num3 = int(input("Enter number three : "))

sum1 = num1 + num2 + num3

if num1 != num2 and num1 != num3 :
    sum2 += num1

if num2 != num1 and num2 != num3 :
    sum2 += num2

if num3 != num1 and num3 != num2:
    sum2 += num3

print("Numbers are", num1, num2, num3)
print("Sum of the three given numbers is : ", sum1)
print("Sum of the non-duplicate numbers is : ", sum2)