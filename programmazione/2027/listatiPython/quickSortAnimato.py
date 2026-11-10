import random

def quicksort(S, start=0, end=None):
    if end is None:
        end = len(S)-1
    if start > end:
        return
    if start == end:
        return
    pivot_pos = partition(S, start, end)
    stampa_lista(s, start, pivot_pos, end, spazi = 4)
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
        for i in range(pivot):
            print(f"{' ':{spazi}s}", end = "")
        print(f"({s[pivot]:{spazi-1}d})")
        
        for i in range(len(s)):
            if i < inizio or i == pivot or i > fine:
                print(f"{' ':{spazi}s}", end = "")
            else:
                print(f"{s[i]:{spazi}d}", end = "")
        print()
    
s = random_list(25, 99)
stampa_lista(s, spazi = 4)
quicksort(s)
stampa_lista(s, spazi = 4)
