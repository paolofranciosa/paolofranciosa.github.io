def crescente(riga):
    cresce = True
    for i in range(len(riga)-1):
        if riga[i] >= riga[i+1]:
            return False
    return True

def num_righe_crescenti(m):
    if not isinstance(m, list):
        raise TypeError
    for r in m:
        if not isinstance(r, list):
            raise TypeError
    num_crescenti = 0
    for riga in m:
        if crescente(riga):
            num_crescenti += 1
    return num_crescenti
