def riga_max_file(nomefile):
    """riceva come
argomento il nome di un file di testo contenente in ciascuna riga
una serie di interi separati da spazio, e restituisca la posizione
della riga con somma massima. Le posizioni di riga si devono
contare a partire da 0. Nel caso di più righe con somma massima
deve essere restituita la posizione della prima di tali righe."""
    file = open(nomefile, "r")
    somma = 0
    s_max = 0
    p_s_max = 0
    file.readlines([n])
    for riga in file:
        for i in riga:
            somma += riga[i]
        return somma
        if somma > s_max:
            somma = s_max
            p_s_max += 1
        if somma == s_max:
            p_s_max = p_s_max
    return p_s_max
    f.close()
    
print(riga_max_file('riga_max_file2.txt'))