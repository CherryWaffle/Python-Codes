x = int(input("Enter value of x: "))
y = int(input("Enter value of y: "))
z = int(input("Enter value of z: "))

print("Individually, A, B and C take", x, y, z, "days respectively")
days = (x*y*z)/(x*y+y*z+x*z)

print("Together A, B and C take", days, "day(s) to finish the work")