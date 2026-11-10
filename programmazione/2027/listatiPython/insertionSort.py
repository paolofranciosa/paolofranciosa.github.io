def insertion_step(L, i):
    """Esegue l'i-esimo passo di insertion sort
    Assume i>0 e che     L[0], L[1], ... L[i-1]       sia ordinata.
    Genera la sequenza   L[0], L[1], ... L[i-1] L[i]  ordinata """
    x = L[i]   # salvo il valore da inserire
    pos =  i   # posizione di inserimento
    
    while pos > 0 and L[pos-1] > x:
        L[pos] = L[pos-1]    # sposto a destra L[pos-1]
        pos = pos -1         # passo all'elemento precedente
    L[pos] = x  # inserisco il nuovo elemento nella posizione corretta
    
    
def insertion_sort(L):
    """Ordina la sequenza L utilizzando insertion sort"""
    for i in range(1,len(L)):
        insertion_step(L,i)

       
        
lista = [5, 3, 67, 8, 1, 2, 4, 2]
print(lista)
insertion_sort(lista)
print(lista)




