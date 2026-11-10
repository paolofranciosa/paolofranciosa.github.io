def coppia_differenza_minima(L):
    valoreconfronto = 10**3
    listafinale = []
    posizionei = 0
    posizionek = 0
    for i in L:
       posizionei += 1
       posizionek = 0
       for k in L:
            if i != k:
                if abs(i) > abs(k):
                    j = abs(i - k)
                else:
                    j = abs(k - i)
                if j < valoreconfronto:
                    valoreconfronto , j = j, valoreconfronto
                    if i < k:
                        listafinale = [posizionei, posizionek]
                    else:
                        listafinale = [posizionek, posizionei]
                    posizionek += 1
    return listafinale

seq = [-5,4,8,-3,1,3,10]
print(coppia_differenza_minima(seq))