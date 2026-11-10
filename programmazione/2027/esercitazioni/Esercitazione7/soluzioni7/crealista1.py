def crealista1(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, int):
        raise TypeError
    if b < 0:
        raise ValueError
    # il valore iniziale si può determinare più facilmente con
    # inizio = math.ceil(a)
    if int(a) == a:
        inizio = a
    elif a > 0:
        inizio = int(a) + 1
    else:
        inizio = int(a)
    risultato = []
    for i in range(inizio, inizio + b):
        risultato.append(i)
    return risultato

