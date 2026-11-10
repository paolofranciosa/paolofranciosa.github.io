def sommaLista(seq, inizio = None, fine = None):
    '''somma degli elementi di una lista aplicando il paradigma divide et impera'''
    if inizio is None:
        inizio = 0
        fine = len(seq) - 1
    if inizio == fine:
        return seq[inizio]
    else:
        med = (inizio + fine) // 2
        return sommaLista(seq, inizio, med) + sommaLista(seq, med + 1, fine)

if __name__ == "__main__":
    s = [3, 2, 4, 56, 8, -2, 0, 9]
    print(sommaLista(s))
