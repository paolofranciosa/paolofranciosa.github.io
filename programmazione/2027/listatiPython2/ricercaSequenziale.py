def ricerca_sequenziale(lista, val):
    '''data una lista, restituisce la posizione della prima occorrenza
    di val nella lista (se esiste), oppure -1 se non esiste'''
    for i in range(len(lista)):
        if val == lista[i]:
            return i
    return -1