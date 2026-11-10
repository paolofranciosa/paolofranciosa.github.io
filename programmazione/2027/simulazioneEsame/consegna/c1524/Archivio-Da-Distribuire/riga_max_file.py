def riga_max_file(nomefile):
    somma_riga = 0
    pos_riga = 0
    giri = 0
    somma_max = 0
    with open(nomefile) as f:
        for riga in f.readlines():
            riga = riga.strip()
            riga = riga.split()
            for numero in riga:
                somma_max = somma_max + int(numero)
            break
    with open(nomefile) as f:
        for riga in f.readlines():
            riga = riga.strip()
            riga = riga.split()
            for numero in riga:
                somma_riga = somma_riga + int(numero)
            if somma_riga > somma_max:
                somma_max = somma_riga
                pos_riga = giri
            giri = giri + 1
            somma_riga = 0
    return pos_riga
                
            
