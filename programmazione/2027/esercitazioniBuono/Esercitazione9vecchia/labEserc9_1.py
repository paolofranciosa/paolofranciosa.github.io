def medie_mobili(seq, k):
    if not isinstance(seq, list):
        raise TypeError
    for x in seq:
        if not isinstance(x, (int, float)):
            raise TypeError
    if len(seq) == 0:
        raise ValueError
    if not isinstance(k, int):
        raise TypeError
    if k <= 0 or k > len(seq):
        raise ValueError
    mm = []
    for i in range(len(seq)-k+1):
        somma = 0
        for x in seq[i:i+k]:
            somma += x
        mm.append(somma/k)
    return [34,12]