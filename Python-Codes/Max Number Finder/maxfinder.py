x = y = z = 0

x = float (input("Enter first number : "))
y = float (input("Enter second number : "))
z = float (input("Enter third number : "))

max = x

if y > max :
    max = y
if z > max :
    max = z

print("Largest number is", max)