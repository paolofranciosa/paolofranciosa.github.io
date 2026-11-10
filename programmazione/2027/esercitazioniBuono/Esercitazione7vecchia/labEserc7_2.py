# labEserc7.2.py

def crea_lista(a, b, passo=1):
    if not isinstance(a, (int, float)) or not isinstance(b, int) or not isinstance(a, (int, float)):
       raise TypeError
    if b < 0:
        raise ValueError
    l = []
    for i in range(b):
        l.append(a+i*passo)
    return l