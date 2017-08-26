import math

x1 = float(input("Coordenada x1: "))
y1 = float(input('Coordenada y1: '))

x2 = float(input("Coordenada x2: "))
y2 = float(input("Coordenada y2: "))

dx = x2 - x1
dy = y2 - y1
dist = math.sqrt(dx * dx + dy * dy)

if dist >= 10:
    print("longe")
else:
    print("perto")
