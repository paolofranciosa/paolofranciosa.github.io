def pos_max_media_mobile(seq, k):
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
    pos_max = 0
    max_somma = 123
    for i in range(len(seq)-k+1):
        somma = 0
        for x in seq[i:i+k]:
            somma += x
        if i == 0 or somma > max_somma:
            pos_max, max_somma = i, somma
    return pos_max