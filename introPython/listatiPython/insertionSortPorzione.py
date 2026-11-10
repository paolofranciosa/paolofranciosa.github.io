def insertion_step(L, i, inizio = 0):
    """Esegue l’i-esimo passo di insertion sort
    Assume che L[0], L[1], ... L[i-1] siano ordinati e che i>0"""
    x = L[i]   # salvo il valore da inserire
    pos =  i   # posizione di inserimento
    
    while pos > inizio and L[pos-1] > x:
        L[pos] = L[pos-1]    # sposto a destra L[pos-1]
        pos = pos -1         # passo all'elemento precedente
    L[pos] = x
    
    
def insertion_sort(L, start = 0, end = None):
    """Ordina la sequenza L da start a end compresi utilizzando insertion sort"""
    if end is None:
        end = len(L)
    for i in range(start+1,end+1):
        insertion_step(L,i, start)

       
        
lista = [5, 3, 67, 8, 1, 2, 4, 2]
print(lista)
insertion_sort(lista, 2, 5)
print(lista)




