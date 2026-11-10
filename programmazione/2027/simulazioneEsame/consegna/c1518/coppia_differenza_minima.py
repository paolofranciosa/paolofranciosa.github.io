def coppia_differenza_minima(L) :
    lista_finale = [0,1]
    differenza_minima = abs(L[0] - L[1])
    
    for i in range(0, len(L)-1) :
        for j in range(i + 1, len(L)-1) :
            if abs(L[i] - L[j]) < differenza_minima :
                differenza_minima = abs(L[i] - L[j])
                lista_finale = [i, j]
    return lista_finale
    
            
        
        