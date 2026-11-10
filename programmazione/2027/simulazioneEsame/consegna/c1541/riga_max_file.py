def riga_max_file(nomefile):
    """riceve come argomento il nome di un file di testo contenente in ciascuna riga
una serie di interi separati da spazio, e restituisca la posizione
della riga con somma massima. Le posizioni di riga si devono
contare a partire da 0. Nel caso di più righe con somma massima
deve essere restituita la posizione della prima di tali righe."""
    with open(nomefile, 'r', encoding="utf-8") as f:
        righe=f.readlines()
        indice_riga_max=None
        massimo=0
        for i in range(len(righe)):
            riga_int=[int(l) for l in righe[i].strip().split(" ")]
            somma_riga=sum(riga_int)
            if somma_riga>massimo:
                massimo=somma_riga
                indice_riga_max=i
        return indice_riga_max
        
print(riga_max_file('riga_max_file2.txt'))

