from math import *

p1 = input().split(" ")
p2 = input().split(" ")

px1 = float(p1[0])
py1 = float(p1[1])

px2 = float(p2[0])
py2 = float(p2[1])

distance = sqrt((px2 - px1) ** 2 + (py2 - py1) ** 2)
print(f"{distance:.4f}")
