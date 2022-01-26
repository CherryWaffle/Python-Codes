x = int(input("Enter Number 1:"))
y = int(input("Enter Number 2:"))
z = int(input("Enter NUmber 3:"))

print("Original Numbers :", x, y, z)
x, y, z = x, x+y, x+y+z

print("After Swapping :", x, y, z)