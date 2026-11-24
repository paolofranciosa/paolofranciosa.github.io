def crea_matrice(r, c, v = 0):
    m = []
    for i in range(r):
        riga = []
        for j in range(c):
            riga.append(v)
        m.append(riga)
    return m

def min_max_altro(mat, i, j):
    '''restituisce -1/+1/0 se mat[i][j] è minimo locale, massimo locale o altro'''
    # assume che mat sia una lista di liste di numeri
    # e che i, j siano inidici di riga e colonna corretti
    
    # prima verifico se è un elemento di bordo
    if i == 0 or j == 0 or i == len(mat) - 1 or j == len(mat[0]) - 1:
        return 0 # elemento di bordo non può essere min/max
    # ora verifico se mat[i][j] > tutti e quattro gli adiacenti
    if mat[i][j] > mat[i-1][j] and mat[i][j] > mat[i+1][j] and mat[i][j] > mat[i][j-1] and mat[i][j] > mat[i][j+1]:
        return 1
    # poi verifico se mat[i][j] < di tutti e quattro gli adiacenti
    if mat[i][j] < mat[i-1][j] and mat[i][j] < mat[i+1][j] and mat[i][j] < mat[i][j-1] and mat[i][j] < mat[i][j+1]:
        return -1
    # se arrivo qui non è né min né max
    return 0

def mat_max_min(a):
    b = crea_matrice(len(a), len(a[0]), 0)
    for i in range(len(a)):
        for j in range(len(a[i])):
            b[i][j] = min_max_altro(a, i, j)
    return b

mappa = [
         [2, 4, 3, 5],
         [2, 6, 2, 9],
         [1, 4, 3, 5],
         [2, 7, 9, 5],
         [2, 4, 1, 5]
        ]
picchi = mat_max_min(mappa)
print(picchi)