import random

def quicksort(S, start=0, end=None):
    if end is None:
        end = len(S)-1
    if start>=end:
        return
    pivot_pos = partition(S, start, end)
    quicksort(S, start, pivot_pos - 1)
    quicksort(S, pivot_pos+1, end)

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