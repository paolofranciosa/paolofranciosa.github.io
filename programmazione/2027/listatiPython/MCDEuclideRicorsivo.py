def MCDEuclide(a,b):
    if a >= b:
        return MCDRicorsivo(a, b)
    else:
        return MCDRicorsivo(b, a)
    
def MCDRicorsivo(a, b):
    print(a, b)  # la stampa serve solo a mostrare il funzionamento dell'algoritmo
    resto = a % b
    if resto == 0:
        return b
    else:
        return MCDRicorsivo(b, resto)
