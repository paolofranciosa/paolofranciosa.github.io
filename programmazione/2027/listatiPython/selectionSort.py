def pos_min(seq, inizio = 0):
    '''data una sequenza di valori (confrontabili) seq e una posizione
    iniziale inizio
    restituisce la prima posizione del valore minimo tra gli elementi
    che compaiono a partire da inizio.
    NON deve modificare seq'''
    posiz = inizio # posiz rapopresenta la posizione del minimo corrente
    for i in range(inizio + 1, len(seq)):
        if seq[i] < seq[posiz]:
            posiz = i # ho trovato un nuovo minimo
    return posiz
    
def selection_sort(L):
    """Ordina la sequenza L utilizzando selection sort"""
    for i in range(len(L) - 1):
        pos = pos_min(L,i)
        if pos != i:
            L[i], L[pos] = L[pos], L[i]
   
        
lista = [5, 3, 67, 8, 1, 2, 4, 2]
print(lista)
selection_sort(lista)
print(lista)




