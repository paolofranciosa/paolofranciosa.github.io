import math
def circle_area(x):
    if not isinstance(x,(int,float)):
        raise TypeError
    if x<0:
        raise ValueError
    return (x**2)*math.pi

