def circle_area(x):
    from math import pi
    if x<0:
        raise ValueError("Not negative number as input")
    area=pi*x**2
    return(area)
