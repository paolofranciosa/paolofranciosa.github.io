def lista_interi(nomefile):
    '''restituisce la lista degli interi contenuti in un file
di testo'''
    f = open(nomefile)
    l =[]
    for riga in f:
        for val in riga.split():
            l.append(int(val))
    return l
