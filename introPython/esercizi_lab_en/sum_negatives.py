def sum_negatives(L):
    total = 0
    for x in L:
        if x < 0:
            total += x
    return total

