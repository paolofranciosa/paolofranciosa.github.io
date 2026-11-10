def verifica_mat_rett(m):
    if not isinstance(m, list) or len(m) <= 0:
        return False
    for riga in m:
        if not isinstance(riga, list) or len(riga) <= 0:
            return False
    ncol = len(m[0])
    for riga in m:
        if len(riga) != ncol:
            return False
    return True

def cerca_pos_max_in_riga(mat, i):
    '''restituisce il numero di colonna in cui si trova il massimo (elemento strettamente maggiore di tutti gli altri elementi) della riga i, se esiste. Se non esiste un elemento strettamente maggiore di tutti gli altri restituisce -1'''
    pos_max = 0
    max = mat[i][0]
    for j in range(1,len(mat[i])):
        if mat[i][j] > max:
            pos_max = j
            max = mat[i][j]
# ora verifica se è strettamente maggiore di tutti gli altri sulla riga i
    for j in range(len(mat[i])):
        if j != pos_max and mat[i][j] == mat[i][pos_max]:
            return -1
    return pos_max
    
def cerca_pos_min_in_colonna(mat, j):
    '''restituisce il numero di riga in cui si trova il minimo (elemento strettamente minore di tutti gli altri elementi) della colonna j, se esiste. Se non esiste un elemento strettamente minore di tutti gli altri restituisce -1'''
    pos_min = 0
    min = mat[0][j]
    for i in range(1,len(mat)):
        if mat[i][j] < min:
            pos_min = i
            min = mat[i][j]
# ora verifica se è strettamente minore di tutti gli altri sulla colonna i
    for i in range(len(mat)):
        if i != pos_min and mat[i][j] == mat[pos_min][j]:
            return -1
    return pos_min
    
def punto_di_sella(mat):
    if not verifica_mat_rett(mat):
        raise TypeError
    for i in range(len(mat)):
        pos_max_in_riga = cerca_pos_max_in_riga(mat,i)
        if pos_max_in_riga != -1:
            pos_min_in_colonna = cerca_pos_min_in_colonna(mat, pos_max_in_riga)
            if pos_min_in_colonna != -1 and pos_min_in_colonna == i:
                return pos_min_in_colonna, pos_max_in_riga
    return None

