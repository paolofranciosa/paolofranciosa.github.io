def frequenza(lista):
    '''a partire da una lista di elementi restituisce un
dizionario contenente il numero di occorrenze
di ciascun elemento'''
    freq = dict()
    for e in lista:
        if e in freq:
            freq[e] = freq[e] + 1
        else:
            freq[e] = 1 # aggiunge nuova chiave
    return freq

if __name__ == "__main__":
    f = frequenza([22,22,44,33,11,22,55,44,66,33,33,11,33])
    print("stampa in ordine qualsiasi")
    for k in f:
        print(k, "compare", f[k], "volte")
    print()
    print("stampa chiavi ordinate")
    for k in sorted(f): 
        print(k, "compare", f[k], "volte")
    