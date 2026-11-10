def dict_sum_small_keys(d, k_threshold):
    somma = 0
    for k in d:
        if k < k_threshold:
            somma += d[k]
    return somma

