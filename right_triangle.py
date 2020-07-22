import random

def right_triangle():
    xcoord1 = random.randint(-10,10)
    ycoord1 = random.randint(-10,10)
    xcoord2 = random.randint(-10,10)
    ycoord2 = random.randint(-10,10)
    xcoord3 = xcoord1
    ycoord3 = ycoord2
    xcoord4 = xcoord2
    ycoord4 = ycoord1

    a = xcoord2 - xcoord1

    if a < 0:
        a = a * -1

    b = ycoord2 - ycoord1

    if b < 0:
        b = b * -1

    c = (a**2 + b**2)**.5

    print("right triangle 1:")
    print("coordinates: " + "(" + str(xcoord1) + "," + str(ycoord1) + ")" + "," + "(" + str(xcoord2) + "," + str(ycoord2) + ")" + "," + "(" + str(xcoord3) + "," + str(ycoord2) + ")")
    print("side lengths: a = " + str(a) + ", b = " + str(b) + ", c = " + str(c))

for i in range(10):
    right_triangle()
    
