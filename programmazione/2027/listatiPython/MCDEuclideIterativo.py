def MCDEuclideIterativo(a, b):
    '''restituisce il Massimo Comun Divisore di due naturali,
applicando l'algoritmo di Euclide in maniera iterativa'''
    if not isinstance(a, int):
        raise TypeError
    if not isinstance(b, int):
        raise TypeError
    if a<=0 or b<=0:
        raise ValueError
    a, b = max(a,b), min(a,b)
    while b > 0 :
        a, b = b, a % b
    return a
