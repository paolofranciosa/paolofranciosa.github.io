def riga_max_file(nomefile) :
    lettura = open (nomefile)
    somma = 0
    verifica =0
    contatore = -1
    risultato = 0
    lista0 =[]
    lista = []
    for i in lettura :
        contatore +=1
        lista0 = i.split()
        for elemento in lista0:
            lista.append (int(elemento))
            
        verifica = sum(lista)
        lista.clear()
        if verifica > somma :
            somma = verifica
            risultato = contatore
    return (risultato)



