def rimuoviDoppie(stringa):
    if len(stringa) == 0:
        return ''
    
    stringa_nuova = stringa[0]
    i = 1
    while i < len(stringa):
        if stringa[i] != stringa[i-1]:
            stringa_nuova = stringa_nuova + stringa[i]
        i += 1
    return stringa_nuova
