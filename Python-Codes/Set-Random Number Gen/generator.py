import random as rand

num1=rand.randrange(10, 70, 13)
num2=rand.randrange(10, 70 ,13)
num3=rand.randrange(10, 70, 13)

set1 = {num1, num2, num3}
print("Random Integers in the range 10 .. 70, \
    step-value 13 :", num1, num2, num3)

print("Set created :", set1)