import math
def circle_area(x):
    if not isinstance(x,(int,float)):
        raise TypeError
    if x<0:
        raise ValueError
    area=x*x*math.pi
    return area

