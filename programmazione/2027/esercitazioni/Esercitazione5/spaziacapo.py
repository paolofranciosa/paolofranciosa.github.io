def spaziacapo(s):
    ris = ''
    for carattere in s:
        if carattere == ' ':
            ris = ris + '\n'
        else:
            ris = ris + carattere
    return ris
