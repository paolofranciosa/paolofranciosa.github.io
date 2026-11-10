def stampa_file(nomefile):
    '''funzione che, a partire dal nome di un file di testo
che si assume sia presente nella stessa cartella del codice,
stampa il contenuto del file'''
    f = open(nomefile)
    for riga in f:
        print(riga, end="")
