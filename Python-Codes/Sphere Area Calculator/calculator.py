import math

r = float(input("Radius of sphere : "))

area = math.pi * r * r
volume = 4 * math.pi * math.pow(r, 3)

print("Radius of the sphere : ", r, "meters")
print("Area of the sphere : ", area,"²")
print("Volume of the sphere : ", volume,"³")