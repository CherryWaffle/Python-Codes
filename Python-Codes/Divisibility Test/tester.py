number1 = int(input("Enter first number : "))
number2 = int(input("Enter second number : "))

remainder = number1 % number2

if remainder == 0 :
    print(number1, "is divisible by", number2)

else : 
    print(number1, "is not divisible by", number2, "and", remainder, "is the remainder")