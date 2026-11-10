import random
def crea_lista_random(lunghezza, val_min=0, val_max=100):
    '''restituisce una lista di interi di lunghezza pari al primo
parametro, contenente valori interi random tra val_min e val_max (compresi)'''
    # ho valori nelle variabili lunghezza, val_min e val_max
    
    lista = []
    for i in range(lunghezza):
        lista.append(random.randint(val_min, val_max))
    return lista