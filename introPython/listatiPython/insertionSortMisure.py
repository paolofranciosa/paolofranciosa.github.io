import random

num_confronti = 0
num_scambi = 0

def num_inversioni(L):
    """restituisce il numero di inversioni di L"""
    n_inv = 0
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[i] > L[j]:
                n_inv += 1
    return n_inv
    
def insertion_step(L, i):
    """Esegue l'i-esimo passo di insertion sort
    Assume che L[0], L[1], ... L[i-1] siano ordinati e che i>0"""
    global num_confronti
    global num_scambi
    x = L[i]   # salvo il valore da inserire
    num_scambi += 1
    pos =  i   # posizione di inserimento
    
    num_confronti+= 1
    while pos > 0 and L[pos-1] > x:
        L[pos] = L[pos-1]    # sposto a destra L[pos-1]
        num_scambi += 1
        pos = pos -1         # passo all'elemento precedente
        num_confronti+= 1
    L[pos] = x
    
    
def insertion_sort(L):
    """Ordina la sequenza L utilizzando insertion sort"""
    for i in range(1,len(L)):
        insertion_step(L,i)

       
def random_list(n, val):
    '''returns a list of n random integers in [1,val]'''
    lista = [None] * n
    for i in range(n):
        lista[i] = random.randint(1, val)
    return lista
    
if __name__ == "__main__":
    maxval = 60
    seq = random_list(25, maxval)
#     seq = sorted(random_list(25, maxval))
#     for i in range(len(seq)):
#         a, b = random.sample(range(len(seq)), 2)
#         seq[a], seq[b] = seq[b], seq[a]
    print(seq)
    inv = num_inversioni(seq)
    insertion_sort(seq)
    print(seq)
    print(f'{num_confronti} confronti')
    print(f'{num_scambi} scambi')
    print(f'{inv} inversioni')
