import math
def circle_area(x):
    if not isinstance(x, (int, float)):
        return ValueError
    if x>0:
        a= math.pi*x**2
    return a
