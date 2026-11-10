import math

def circle_area(x):
    if x<0:
        raise TypeError
    else:
        area=math.pi*(x*x)
    return area
circle_area(2)