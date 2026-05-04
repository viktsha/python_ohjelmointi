import math

def create_point(x, y):
    return (x, y)

def distance(p1, p2):
    d = math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
    return d

x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))

p1 = create_point(x1, y1)
p2 = create_point(x2, y2)

d = distance(p1, p2)
print (f"Pisteiden välinen etäisyys: {d: .2f}")
