# labEserc6_4.py

def unione(a, b):
    if not isinstance(a, list) or not isinstance(b, list):
        raise TypeError
    
    union = []
    for x in a:
        if x not in union:
            union.append(x)
    for x in b:
        if x not in union:
            union.append(x)
    return union