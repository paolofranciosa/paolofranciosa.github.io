def ricerca_binaria(lista, val):
    '''data una lista che si suppone ordinata in senso crescente,
    restituisce la posizione di una occorrenza
    di val nella lista (se esiste), oppure None se non esiste'''
    inizio = 0
    fine = len(lista) - 1
    while inizio <= fine:
        med = (inizio + fine) // 2
        if val < lista[med]:
            fine = med - 1
        elif val > lista[med]:
            inizio = med + 1
        else:
            return med
    return None
