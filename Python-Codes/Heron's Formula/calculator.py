import math

a = int(input("Side 1 : "))
b = int(input("Side 2 : "))
c = int(input("Side 3 : "))

s = (a + b + c)/2
area = math.sqrt(s * (s-a) * (s-b) * (s-c)) 

print("The three sides are", a, b, c)
print("Area :", area, "units square")