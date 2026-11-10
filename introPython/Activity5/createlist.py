import math

def createlist(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, int):
        raise TypeError
    if b < 0:
        raise ValueError
    l = []
    a = math.ceil(a)
    for i in range(b):
        l.append(a + i)
    return l

