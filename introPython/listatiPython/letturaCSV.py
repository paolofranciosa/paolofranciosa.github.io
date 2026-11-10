def stampa_valori_da_file(nomefile):
    '''legge valori numerici da un file CSV con campi separati da ";",
scartando la riga di intestazione, e li stampa'''
    f = open(nomefile)
    prima_riga = f.readline() # scarta la prima riga
    for riga in f:
        # nella stringa riga deve essere eliminato l'ultimo carattere (\n)
        lista = riga[:-1].split(sep = ";") # lista delle stringhe separando su ";"
        valori = [] # lista dei valori numerici nella riga
        for elem in lista:
            valori.append(int(elem))
        
        # stampa di controllo
        for v in valori:
            print(v, " ", end = "")
        print() # a capo a fine riga

stampa_valori_da_file("datiProva.txt") # assume che esista un file di testo
                                       # datiProva.txt nella stessa cartella