def coppia_differenza_minima(L):
    coppia = []
    differenzamin = float('inf')
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            differenza = abs(L[i] - L[j])
            if differenza < differenzamin :
                differenzamin = differenza
                coppia = [i,j]
            
    return coppia
            
        
        
        