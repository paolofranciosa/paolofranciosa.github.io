import math

def circle_area(x):
    pi=math.pi
    if x <1:
        raise ValueError
    else:
        area=pi*x**2
    return area
