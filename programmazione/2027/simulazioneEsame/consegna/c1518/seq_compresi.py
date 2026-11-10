def seq_compresi(L, low, high) :
    risultato = 0
    for valore in L :
        if valore >= low and valore <= high :
            risultato += 1
            
    return risultato

print(seq_compresi([1,2,3,4,5,6], 2, 5))
            