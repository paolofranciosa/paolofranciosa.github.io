def less_non_zero(r, k):
    count = 0
    for el in r:
        if el != 0:
            count += 1
    if count < k:
        return True
    else:
        return False

def mat_dense_rows(m, k):

    for r in m:
        if less_non_zero(r, k):
            return False
    return True

