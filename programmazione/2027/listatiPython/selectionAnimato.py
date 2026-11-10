import random

def selection(S, k):
    '''restituisce il valore del k-esimo elemento, ad esempio il mediano se k e' la meta' della lunghezza della sequenza.
    Si assume che k sia compreso tra start ed end (oppure len(S)-1).
    Per evitare che la lista venga modificata, ne crea una copia e chiama la funzione sulla copia'''
    copia = S.copy()
    return selectionQuick(copia, k, 0, len(copia)-1)

def selectionQuick(S, k, start, end):
    '''restituisce il valore del k-esimo elemento, ad esempio il mediano se k e' la meta' della lunghezza della sequenza.
    Si assume che k sia compreso tra start ed end, estremi inclusi.'''
    pivot_pos = partition(S, start, end)
    stampa_lista(S, start, pivot_pos, end, 3)
    if k == pivot_pos:
        return S[pivot_pos]
    elif k < pivot_pos:
        return selectionQuick(S, k, start, pivot_pos - 1)
    else:
        return selectionQuick(S, k, pivot_pos+1, end)

def partition(S, start, end):
    # sceglie una posizione random per il pivot
    pivot_pos = random.randint(start, end)
    pivot = S[pivot_pos]
    # scambia il pivot con l'elemento di testa
    S[start], S[pivot_pos] = S[pivot_pos], S[start]
    i = start+1
    j = end
    # scansione della lista dall'inizio (pivot escluso) verso il centro
    # e dalla fine verso il centro
    while i<j:
        while i<j and S[i] < pivot: # cerca elemento >= pivot
            i += 1
        while i<j and S[j] >= pivot: # cerca elemento < pivot
            j -= 1
        if i<j:
            # se ha trovato una coppia da scambiare la scambia
            S[i], S[j] = S[j], S[i]
    if S[i] >= pivot: # decide se il pivot deve andare in posizione i oppure i-1
        i -= 1
    S[start], S[i] = S[i], S[start] # posiziona il pivot al centro
    return i

def random_list(n, maxval):
    s = [0] * n
    for i in range(len(s)):
        s[i] = random.randint(1, maxval)
    return s
    
def stampa_lista(s, inizio = 0, pivot = 0, fine = None, spazi = 5):
    if fine is None:
        for i in range(len(s)):
            print(f"{s[i]:{spazi}d}", end = "")
        print()
    else:
#        for i in range(pivot):
#            print(f"{' ':{spazi}s}", end = "")
#        print(f"({s[pivot]:{spazi-1}d})")
        print(f"{'pivot = '+str(s[pivot]):>{spazi*(pivot+1)}s}")
        for i in range(len(s)):
            if i < inizio or i == pivot or i > fine:
                print(f"{' ':{spazi}s}", end = "")
            else:
                print(f"{s[i]:{spazi}d}", end = "")
        print()
    
lungh = 35
s = random_list(lungh, 99)
p = random.randint(0, lungh - 1)
print(f'cerco elemento di rank {p} in')
stampa_lista(s, spazi = 3)
selection(s, p)
