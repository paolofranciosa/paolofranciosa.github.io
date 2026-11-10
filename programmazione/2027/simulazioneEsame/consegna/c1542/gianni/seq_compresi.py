def seq_compresi(L,low,high):
    conta = 0
    for e in L:
        if e >= low and e <= high:
            conta += 1
        
    return conta