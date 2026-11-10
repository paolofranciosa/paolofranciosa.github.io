def frequenza_parole(frase):
    '''data una lista di parole,
       restituisce un dizionario contenente un item
       per ciascuna parola, e la frequenza associata'''
    frequenze = {}   # crea un dict (dizionario) vuoto
    for p in frase: 
        if p in frequenze:  # se nel dict frequenze e' presente una chiave p
            frequenze[p] = frequenze[p] + 1 # modifica il valore associato alla chiave p
        else:               # non e' presente una chiave p
            frequenze[p] = 1   # aggiunge al dict una nuova voce con chiave p e valore 1
    return frequenze

def frequenze_in_frase(frase):
    '''data una stringa con parole e spazi,
       restituisce un dizionario contenente un item
       per ciascuna parola, e la frequenza associata'''
    lista_parole = frase.split()
    return frequenza_parole(lista_parole)

def stampa_dizionario(ddd):
    for chiave in ddd:
        print(chiave, ddd[chiave])

def stampa_ordinata_dizionario(ddd):
    for chiave in sorted(ddd):
        print(chiave, ddd[chiave])

def stampa_altra_dizionario(ddd):
    for chiave in ddd:
        print(f"chiave {chiave}: valore {ddd[chiave]}")
        
if __name__ == "__main__":
    freq = frequenze_in_frase("Roma Firenze Firenze Milano Roma Roma Milano Bari Napoli Bari")
    print("="*10)
    print(freq)
    print("="*10)
    stampa_dizionario(freq)
    print("="*10)
    stampa_ordinata_dizionario(freq)
    print("="*10)
    stampa_altra_dizionario(freq)
    print("="*10)
