import random
def lista_random(lungh, min, max):
    lista = []
    for i in range(lungh):
        lista.append(random.randint(min, max))
    return lista