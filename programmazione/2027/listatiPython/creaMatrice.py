def crea_mat_zero(n,m):
    ''' crea e restituisce una matrice n x m contenente zeri'''
    mat = []
    for i in range(n):
        riga = []
        for j in range(m):
            riga.append(0)
        mat.append(riga)
    return mat

if __name__ == "__main__":
    m1 = crea_mat_zero(2,3)
    print(m1)
    m2 = crea_mat_zero(1,5)
    print(m2)
    m3 = crea_mat_zero(3,1)
    print(m3)