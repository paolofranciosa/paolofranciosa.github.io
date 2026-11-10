def seq_compresi(sequenza, low, high):

    cnt = 0
    for v in sequenza:
        if low <= v <= high:
            cnt += 1
    return cnt

