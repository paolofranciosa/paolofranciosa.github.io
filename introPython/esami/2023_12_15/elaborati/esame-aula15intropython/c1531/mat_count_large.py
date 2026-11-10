def mat_count_large(m, treshold):
    contatore = 0
    for riga in m:
        for el in riga:
            if el > treshold:
                 contatore = contatore + 1
    return contatore




Ma = [ [2,1], [1,3] ]

print(mat_count_large(Ma, 1))

