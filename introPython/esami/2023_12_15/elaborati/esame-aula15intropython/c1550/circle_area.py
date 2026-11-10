'''Write a function circle_area(x) that:
• takes a non-negative number x as parameter;
• returns the area of a circle with radius x.
After importing math package, a good approximation of Pi is available as
math.pi'''

def circle_area(x):
    import math
    area=math.pi*(x**2)
    return area