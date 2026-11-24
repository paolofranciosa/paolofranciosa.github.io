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

