import math
def circle_area(x):
    if x < 0:
        raise ValueError
    else:
        pi = math.pi
        r = pi*(x**2)
        return r
        