def coppia_differenza_minima(L):
    differenza = 0
    contatore = -1
    lista = []
    minimo = 0
    for i in L :
       
        lista_prova = []
        elemento = 0
        elemento = i
        lista_prova= L.copy()
        lista_prova.remove(elemento)
        for j in lista_prova:
            contatore +=1
            differenza = abs (elemento - j )
            if contatore == 0 :
                minimo = differenza
                lista.append (L.index(i))
                lista.append (L.index(j))
                continue
            elif differenza < minimo :
                minimo = differenza
                lista.clear()
                lista.append (L.index(i))
                lista.append (L.index(j))
    return lista




                