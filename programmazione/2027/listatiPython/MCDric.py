def MCDEuclide(a,b):
    if a >= b:
        return MCDRicorsivo(a, b)
    else:
        return MCDRicorsivo(b, a)
    
def MCDRicorsivo(a, b):
    print(a, b)
    resto = a % b
    if resto == 0:
        return b
    else:
        return MCDRicorsivo(b, resto)
    
print(MCDEuclide(1400, 845))
