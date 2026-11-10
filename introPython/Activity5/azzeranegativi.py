def azzeranegativi(valori):
    if not isinstance(valori, list):
        raise TypeError
    for x in valori:
        if not isinstance(x, (int, float)):
            raise TypeError
    for i in range(len(valori)):
        if valori[i] < 0:
            valori[i] = 0

