# labEserc6_4.py

def intersezione(a, b):
    if not isinstance(a, list) or not isinstance(b, list):
        raise TypeError
    
    inters = []
    for x in a:
        if x not in inters and x in b:
            inters.append(x)
    inters.sort()
    return inters
