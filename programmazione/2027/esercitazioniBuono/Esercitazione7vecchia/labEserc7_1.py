# labEserc7.1.py

def crea_lista(a,b):
    if not isinstance(a, (int, float)) or not isinstance(b, int):
       raise TypeError
    if b < 0:
         raise ValueError
    l = []
    for i in range(b):
        l.append(a+i)
    return l