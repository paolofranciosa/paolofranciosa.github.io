def coppia_differenza_minima(L):
    pos_i = 0
    pos_j = 0
    lista = []
    diff = 0
    diff_min = max(L)-min(L)
    if len(L) == 2:
        lista = [0, 1]
        return lista
    for numero in range(len(L)):
        for resto in range(numero+1, len(L)):
            diff = abs(L[numero] - L[resto])
            if diff < diff_min:
                diff_min = diff
                pos_i = numero
                pos_j = resto
    if pos_i < pos_j: #non servirebbe questo if, dal momento che resto va da numero in poi, dunque è sempre maggiore di numero
        lista.append(pos_i)
        lista.append(pos_j)
    else:
        lista.append(pos_j)
        lista.append(pos_i)
    return lista
    
