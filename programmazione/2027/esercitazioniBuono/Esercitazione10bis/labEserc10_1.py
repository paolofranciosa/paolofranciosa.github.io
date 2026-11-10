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
