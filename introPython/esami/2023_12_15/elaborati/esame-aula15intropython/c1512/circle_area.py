import math

def circle_area(x):
    if x >= 0:
        print(math.pi * x**2)
    else:
        raise ValueError
