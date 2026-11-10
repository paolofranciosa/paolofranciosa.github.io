def somma_interi(nome_file):
    '''si aspetta che esista un file di nome nome_file (str)
contenente un intero per ciascuna riga, e restituisce la somma di tali interi'''
    somma = 0
    # legge una riga alla volta e la aggiunge a somma
    f_input = open(nome_file, "r", encoding="utf-8")
    for riga_letta in f_input: # legge una riga (str) alla volta e la assegna a
                              # VARIABILE
        somma += int(riga_letta)
    return somma
    
def leggi_file(nome_file):
    '''si aspetta che esista un file di nome nome_file (str)
e ne stampa il contenuto'''
    # legge una riga alla volta e la aggiunge a somma
    f_input = open(nome_file, "r", encoding="utf-8")
    for riga_letta in f_input: # legge una riga (str) alla volta incluso \n
                              # e la assegna a VARIABILE
        riga = riga_letta.strip() # copia senza whitespace in testa e in coda
        print(riga) # stampa riga e poi va a capo
    f_input.close()
    return

leggi_file("pippo.txt") # stampa 45
s = somma_interi("pippo.txt")
print(s)

