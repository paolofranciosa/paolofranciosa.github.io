import time
import random

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

def merge(S,inizio, mid, fine):
    '''S contiene una sequenza crescente dalla posizione inizio alla posizione mid comprese, e una sequenza crescente dalla posizione mid+1 alla posizione fine comprese.
    Gli elementi di queste due sequenze vengono fusi in una sola sequenza dalla posizione inizio alla posizione fine comprese'''
    i=inizio
    j=mid+1
    temp=[]
    # Parte 1 - Inserisci in testa il piu' piccolo
    while i<=mid and j<=fine:
        if S[i]<=S[j]:
            temp.append(S[i])
            i += 1
        else:
            temp.append(S[j])
            j += 1
    # Parte 2 - Esattamente UNA sequenza e' esaurita. Va aggiunta la coda residua di una delle due sequenze
    if i > mid:
        residuo = range(j, fine+1)
    else:
        residuo = range(i, mid+1)
    for k in residuo:
        temp.append(S[k])
    # Parte 3 - Va tutto copiato su S[inizio:fine+1]
    for k in range(len(temp)):
        S[inizio+k] = temp[k]

def mergesort(S, inizio=0, fine=None):
    '''realizza l'algoritmo di ordinamento per fusione'''
    if fine == None:
        fine = len(S)-1
    if inizio < fine:
        mid=(inizio+fine)//2
        mergesort(S, inizio, mid)
        mergesort(S, mid+1, fine)
        merge(S, inizio, mid, fine)

def mergesortinsertion(S, inizio=0, fine=None, base = 5):
    '''realizza l'algoritmo di ordinamento per fusione, se meno di base elementi applica insertion sort'''
    if fine == None:
        fine = len(S)-1
    if inizio + base - 1 < fine:
        mid=(inizio+fine)//2
        mergesort(S, inizio, mid)
        mergesort(S, mid+1, fine)
        merge(S, inizio, mid, fine)
    elif inizio + 1 == fine:
        if S[inizio] > S[fine]:
            S[fine], S[inizio] = S[inizio], S[fine]
    elif inizio < fine:
        insertion_sort(S, inizio, fine)

def random_list(lunghezza, minimo, massimo):
    lista = [0]*lunghezza
    for i in range(len(lista)):
        lista[i] = random.randint(minimo, massimo)
    return lista


lista = random_list(1000000, 0, 1000000)
# prova applicando il passo base per lunghezza da 3 a 20
for l_base in range(3,20):
    copia = lista.copy()
    inizio = time.time_ns()
    mergesortinsertion(copia, base=l_base)
    fine = time.time_ns()
    print(f'base {l_base}: {(fine-inizio)/1000000:.3f} sec')

