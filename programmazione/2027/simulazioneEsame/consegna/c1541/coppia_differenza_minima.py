def coppia_differenza_minima(L):
    diff_abs_coppie=abs(L[1]-L[0])
    indice_coppia=[0,1]
    for k in range(1,len(L)):
        for g in range(1,len(L)):
            if k!=g:
                diff=abs(L[k]-L[g])
                if diff<diff_abs_coppie:
                    diff_abs_coppie=diff
                    indice_coppia=[k,g]
    if indice_coppia[0]<indice_coppia[1]:
        return indice_coppia
    else:
        return [indice_coppia[1],indice_coppia[0]]

seq = [-5,4,8,-3,1,3,10]
print(coppia_differenza_minima(seq))