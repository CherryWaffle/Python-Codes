print("Enter The 10 numbers below -> ")

num1 = float(input("First Number : "))
num2 = float(input("Second Number : "))
num3 = float(input("Third Number : "))
num4 = float(input("Fourth Number : "))
num5 = float(input("Fifth Number : "))
num6 = float(input("Sixth Number : "))
num7 = float(input("Seventh Number : "))
num8 = float(input("Eighth Number : "))
num9 = float(input("Ninth Number : "))
num10 = float(input("Tenth Number : "))

divisor = float(input("Enter divisor numer : "))
count = 0

print("Multiples of", divisor, "are : ")

remainder = num1 % divisor
if remainder == 0:
    print(num1, sep = " ")
    count += 1

remainder = num2 % divisor
if remainder == 0:
    print(num2, sep = " ")
    count += 1

remainder = num3 % divisor
if remainder == 0:
    print(num3, sep = " ")
    count += 1

remainder = num4 % divisor
if remainder == 0:
    print(num4, sep = " ")
    count += 1

remainder = num5 % divisor
if remainder == 0:
    print(num5, sep = " ")
    count += 1

remainder = num6 % divisor
if remainder == 0:
    print(num6, sep = " ")
    count += 1

remainder = num7 % divisor
if remainder == 0:
    print(num7, sep = " ")
    count += 1

remainder = num8 % divisor
if remainder == 0:
    print(num8, sep = " ")
    count += 1

remainder = num9 % divisor
if remainder == 0:
    print(num9, sep = " ")
    count += 1

remainder = num10 % divisor
if remainder == 0:
    print(num10, sep = " ")
    count += 1

print()

print(count, "multiples of", divisor, "found")