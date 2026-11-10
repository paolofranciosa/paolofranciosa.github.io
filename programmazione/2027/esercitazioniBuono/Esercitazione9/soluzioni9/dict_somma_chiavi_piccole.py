def dict_somma_chiavi_piccole(d, k_soglia):
    somma = 0
    for k in d:
        if k < k_soglia:
            somma += d[k]
    return somma

