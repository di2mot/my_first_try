# Heron's formula for finding the area of a triangle
a = int(input())
b = int(input())
c = int(input())
p = (a + b + c)/2 # half area
S = (p * ((p - a) * (p - b) * (p - c))) ** 0.5 # the area of the triangle
print(S)
