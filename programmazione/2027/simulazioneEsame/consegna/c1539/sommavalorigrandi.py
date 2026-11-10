def sommavalorigrandi (D, soglia) :
    somma = 0
    for elemento in D.values() :
        if elemento > soglia :
            somma += elemento
    return (somma)

