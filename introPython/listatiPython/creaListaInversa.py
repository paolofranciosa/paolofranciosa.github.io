def crea_lista_inversa(l):
    '''restituisce una copia della lista parametro, in ordine inverso.'''
    risultato = []
    i = len(l)-1
    while i >= 0:
        risultato.append(l[i])
        i -= 1
    return risultato

