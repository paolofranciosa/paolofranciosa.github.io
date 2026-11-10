# labEserc7.4.py

def posiz_minimo(valori, start=0):
    if not isinstance(valori, list):
        raise TypeError
    if len(valori) == 0:
        raise ValueError
    if start < 0 or start >= len(valori):
        raise ValueError
    for x in valori:
        if not isinstance(x, (int, float)):
            raise TypeError
    pos_min = start
    for i in range(start, len(valori)):
        if valori[i] < valori[pos_min]:
            pos_min = i
    return pos_min
