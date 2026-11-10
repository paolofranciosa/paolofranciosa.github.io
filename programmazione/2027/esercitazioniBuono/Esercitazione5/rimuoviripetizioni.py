def rimuoviripetizioni(stringa):
    if len(stringa) == 0:
        return ''
    
    stringa_nuova = stringa[0]
    for carattere in stringa:
        if not (carattere in stringa_nuova):
            stringa_nuova = stringa_nuova + carattere
            
    return stringa_nuova 
