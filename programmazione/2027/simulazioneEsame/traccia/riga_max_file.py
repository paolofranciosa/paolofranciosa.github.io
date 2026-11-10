def somma(riga):
    nums = riga.split()
    s = 0
    for el in nums:
        s += int(el)
    return s

def riga_max_file(nomefile):
    if not isinstance(nomefile, str):
        raise TypeError
    lista_somme = []
    with open(nomefile) as f:
        for r in f:
            lista_somme.append(somma(r))
    max_somma = lista_somme[0]
    max_riga = 0
    for i in range(len(lista_somme)):
        if lista_somme[i] > max_somma:
            max_somma = lista_somme[i]
            max_riga = i
    return max_riga
