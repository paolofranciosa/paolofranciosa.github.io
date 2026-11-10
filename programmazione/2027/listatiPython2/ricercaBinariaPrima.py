def ricerca_binaria_prima(lista, val):
    '''data una lista che si suppone ordinata in senso crescente,
    restituisce la posizione della prima occorrenza
    di val nella lista (se esiste), oppure -1 se non esiste'''
    inizio = 0            # posizione del primo elemento utile nella lista
    fine = len(lista) - 1 # posizione dell'ultimo elemento utile nella lista
    while inizio <= fine:
        med = (inizio + fine) // 2
        if val < lista[med] or med > inizio and val == lista[med-1]:
            fine = med - 1
        elif val > lista[med]:
            inizio = med + 1
        else:
            return med
    return -1

print(ricerca_binaria_prima([1,1,1,2,2,5,5,5,6,7,7,7,8], 1))