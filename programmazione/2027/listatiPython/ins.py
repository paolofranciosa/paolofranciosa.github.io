import random
def seq_random(lungh):
    s = []
    for i in range(lungh):
        s.append(random.random())
    return s

def insertion_step(L, i):
    """Esegue l’i-esimo passo di insertion sort
    Assume che L[0], L[1], ... L[i-1] siano ordinati e che i>0"""
    x = L[i]   # salvo il valore da inserire
    pos =  i   # posizione di inserimento
    
    while pos > 0 and L[pos-1] > x:
        L[pos] = L[pos-1]    # sposto a destra L[pos-1]
        pos = pos -1         # passo all'elemento precedente
    L[pos] = x
    
    
def insertion_sort(L):
    """Ordina la sequenza L utilizzando insertion sort"""
    for i in range(1,len(L)):
        insertion_step(L,i)
        
lista = seq_random(300000)
print("inizio")
lista.sort()
print("finito")