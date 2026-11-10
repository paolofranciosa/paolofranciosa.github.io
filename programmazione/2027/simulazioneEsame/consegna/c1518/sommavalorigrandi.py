def sommavalorigrandi(D, soglia) :
    somma_finale = 0
    lista_valori = D.values()
    for valore in lista_valori :
        if valore > soglia :
            somma_finale += valore
            
    return somma_finale

