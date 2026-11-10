def spezza_in_parole(frase):
    if not isinstance(frase, str):
        raise TypeError
    risultato = frase.split()
    return risultato

