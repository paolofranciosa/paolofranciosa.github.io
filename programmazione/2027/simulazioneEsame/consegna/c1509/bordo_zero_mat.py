def bordo_zero_mat(M):
    """prenda come argomento una matrice rettangolare di dimensioni R×C con R ≥ 1
e C ≥ 1 , che restituisca True se il bordo della matrice è costituito
esclusivamente da zeri, e che restituisca False altrimenti."""
    for i in M[0]:
        if i != 0:
            return False
    for i in M[-1]:
        if i != 0:
            return False
    return True
                
M1 = [[0]]
M2 = [[0,0,0,0], [0,7,8,0] , [0,0,0,0]]
M3 = [[1,0,0], [0,8,0] , [0,2,-1], [0,0,0]]
print(bordo_zero_mat(M1))
print(bordo_zero_mat(M2))
print(bordo_zero_mat(M3))