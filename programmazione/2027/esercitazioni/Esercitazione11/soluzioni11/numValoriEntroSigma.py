import math

def media(s):
    return sum(s) / len(s)

def std_dev(s):
    somma_quadrati = 0
    m = media(s)
    for e in s:
        somma_quadrati += (e - m) * (e - m)
    return math.sqrt(somma_quadrati / len(s))

def conta_fuori_intervallo(lista):
    m = media(lista)
    sigma = std_dev(lista)
    sinistro = m - sigma
    destro = m + sigma
    print(sinistro, destro)
    conta = 0
    for e in lista:
        if e < sinistro or e > destro:
            conta += 1
    return conta

def estrai_colonna(m, j):
    col = []
    for r in m:         # per ciascuna riga
        col.append(r[j])  # copia il j-mo elemento della riga
    return col

def fuori_sigma_su_righe(mat):
    ris = []
    for riga in mat:
        ris.append(conta_fuori_intervallo(riga))
    return ris

def fuori_sigma_su_colonne(mat):
    ris = []
    for j in range(len(mat[0])):
        colonna = estrai_colonna(mat, j)
        ris.append(conta_fuori_intervallo(colonna))
    return ris


tab = [
         [2, 4, 3, 5],
         [2, 6, 2, 5],
         [1, 4, 3, 5],
         [2, 7, 2, 5],
         [2, 4, 1, 5]
      ]

print(tab)
fr = fuori_sigma_su_righe(tab)
print(fr)
print()
fc = fuori_sigma_su_colonne(tab)
print(fc)
