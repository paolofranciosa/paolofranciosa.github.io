def seq_compresi(L, low, high):
    compresi = 0
    for i in L:
        if i >= low and i <= high:
            compresi = compresi + 1
    return compresi

