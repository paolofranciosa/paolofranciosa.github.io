def bordo_zero_mat(M):
    """prende come argomento una matrice rettangolare di dimensioni R×C con R ≥ 1 e
C ≥ 1 , che restituisca True se il bordo della matrice è costituito
esclusivamente da zeri, e che restituisca False altrimenti."""
    r=len(M)
    c=len(M[0])
    if M[0]!=[0]*c or M[len(M)-1]!=[0]*c:
        return False
    for riga in M:
        if riga[0]!=0 or riga[c-1]!=0:
            return False
    return True
    
M1 = [[0]]
M2 = [[0,0,0,0], [0,7,8,0] , [0,0,0,0]]
M3 = [[1,0,0], [0,8,0] , [0,2,-1], [0,0,0]]
print(bordo_zero_mat(M1))
print(bordo_zero_mat(M2))
print(bordo_zero_mat(M3))