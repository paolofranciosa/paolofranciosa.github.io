def stampa_file(nomefile):
    '''funzione che, a partire dal nome di un file di testo
che si assume sia presente nella stessa cartella del codice,
visualizza il contenuto del file'''
    f = open(nomefile, "r")
    for riga in f:
        print(riga, end="") # end="" poiche' la str riga letta da f contiene anche il carattere "\n"

def scrivi_file(nomefile, stringa):
    '''funzione che, a partire dal nome di un file,
crea un file e vi scrive il contenuto di stringa
Il file viene creato nella stessa cartella del codice
'''
    f = open(nomefile, "w")
    print(stringa, file = f) 
    f.close()  # e' importante chiudere il file quando sono terminate tutte le operazioni di scrittura.

nomefile_in = input("digita il nome del file da leggere, compresa l'estensione: ")
stampa_file(nomefile_in)
nomefile_out = input("digita il nome del file da scrivere, compresa l'estensione: ")
scrivi_file(nomefile_out, "stringa qualsiasi\nper provare")
