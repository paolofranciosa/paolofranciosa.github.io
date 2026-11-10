def dict_quadrati(n):
    if not isinstance(n, int):
        raise TypeError
        
    if n < 0:
        raise ValueError
        
    d = dict()
    for i in range(1, n + 1):
        d[i] = i * i
    return d
 

