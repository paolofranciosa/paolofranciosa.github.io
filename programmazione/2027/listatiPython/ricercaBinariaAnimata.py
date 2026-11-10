import random

def stampa_porzione(seq, inizio, fine):
    print("[", end = "")
    for i in range(len(seq)):
        if i >= inizio and i <= fine:
            print(f'{seq[i]:3d} ', end = "")
        else:
            print(f'{"":4s}', end = "")
    print("]")

def ricerca_binaria(lista, val):
    '''data una lista che si suppone ordinata in senso crescente,
    restituisce la posizione di una occorrenza
    di val nella lista (se esiste), oppure -1 se non esiste'''
    inizio = 0
    fine = len(lista) - 1
    while inizio <= fine:
        stampa_porzione(lista, inizio, fine)
        med = (inizio + fine) // 2
        if val < lista[med]:
            fine = med - 1
        elif val > lista[med]:
            inizio = med + 1
        else:
            return med
    stampa_porzione(lista, 0, -1)
    return -1

def random_list(n, val):
    '''returns a list of n random integers in [10,val+10]'''
    lista = [None] * n
    for i in range(n):
        lista[i] = random.randint(1, val) + 10
    return lista
    
if __name__ == "__main__":
    maxval = 35
    seq = sorted(random_list(25, maxval))
    x = random.randint(1, maxval) + 10
    print(f'cerco {x}')
    print("i valori stampati indicano l'intervallo di ricerca\n")
    print("trovato in posizione", ricerca_binaria(seq, x))