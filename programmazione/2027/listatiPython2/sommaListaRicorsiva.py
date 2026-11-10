def sommaLista(seq, inizio = None, fine = None):
    '''somma degli elementi di una lista di liste di liste ....
Se inizio e fine sono None si intende l'intera lista'''
    if inizio is None:
        inizio = 0
        fine = len(seq) - 1
    if inizio > fine: # lista vuota o intervallo vuoto
        return 0
    if inizio == fine: # un solo elemento: potrebbe essere un numero o una lista
        if isinstance(seq[inizio], (int, float)):
            return seq[inizio]
        else: # in questo caso è una lista
            return sommaLista(seq[inizio])
    else:
        med = (inizio + fine) // 2
        return sommaLista(seq, inizio, med) + sommaLista(seq, med + 1, fine)

if __name__ == "__main__":
    s = [3, 2, 4, 56, 8, -2, 0, 9]
    print(sommaLista(s))
    s = [3, [[2, 4], [], 56], 8, [-2], 0, 9]
    print(sommaLista(s))
