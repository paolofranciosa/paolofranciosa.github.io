def sommavalorigrandi(D,soglia):
    acc=0
    for k in D:
        if D[k]>soglia:
            acc += D[k]
    return acc
