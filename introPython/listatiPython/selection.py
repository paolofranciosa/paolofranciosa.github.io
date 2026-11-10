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