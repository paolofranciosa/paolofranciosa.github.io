def seq_compresi (L, low, high) :
    lista = []
    if len(L)==0 :
        return 0
    for i in L :
        if i >= low and i <= high :
            lista.append(i)
    numero = len (lista)
    return (numero)
        
        
        
    
        
        
    