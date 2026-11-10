def bordo_zero_mat(M):
    '''prenda come argo-
mento una matrice rettangolare di dimensioni R×C con R ≥ 1 e
C ≥ 1 , che restituisca True se il bordo della matrice è costituito
esclusivamente da zeri, e che restituisca False altrimenti.'''
    for x in M[0]:
        if x != 0:
            return False
    for x in M[-1]:
        if x != 0:
            return False
    return True

M1 = [[0]]
M2 = [[0,0,0,0], [0,7,8,0] , [0,0,0,0]]
M3 = [[1,0,0], [0,8,0] , [0,2,-1], [0,0,0]]
print(bordo_zero_mat(M1))
print(bordo_zero_mat(M2))
print(bordo_zero_mat(M3))
    
    
    
    
#    for righe in M:
#        for colonne in righe:
#            if righe == 0 or righe == len(M)-1:
                
    