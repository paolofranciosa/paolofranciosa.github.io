def sostituisci_con_spazi(frase):
    if not isinstance(frase, str):
        raise TypeError
    risultato = ""
    for c in frase:
        if c.isalpha():
            risultato = risultato + c
        else:
            risultato = risultato + " "
    return risultato
    
def copia_minuscola(frase):
    if not isinstance(frase, str):
        raise TypeError
    risultato = ""
    for c in frase:
        if "A" <= c and c <= "Z":
            risultato = risultato + c.lower()
        else:
            risultato = risultato + c
    return risultato

def spezza_in_parole(frase):
    if not isinstance(frase, str):
        raise TypeError
    risultato = frase.split()
    return risultato

def parole_ordinate(lista_parole):
    if not isinstance(lista_parole, list):
        raise TypeError
    risultato = []
    for x in lista_parole:
        risultato.append(x)
    risultato.sort()
    return risultato

def elimina_duplicati(lista_parole):
    if not isinstance(lista_parole, list):
        raise TypeError
    risultato = []
    prec = None
    for x in lista_parole:
        if x != prec:
            risultato.append(x)
        prec = x
    return risultato

def elenco_parole_presenti(frase):
    return elimina_duplicati(parole_ordinate(spezza_in_parole(copia_minuscola(sostituisci_con_spazi(frase)))))