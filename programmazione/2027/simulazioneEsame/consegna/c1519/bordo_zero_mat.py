def bordo_zero_mat(M):
    '''prende come argomento una matrice
rettangolare di dimensioni R×C con R ≥ 1
e C ≥ 1 , che restituisce True se il bordo
della matrice è costituito esclusivamente
da zeri, e che restituisca False
altrimenti.'''
    for i in range(len(M)-1):
       if M[i[0]]== 0 and M[i[len-1]]== 0:
           return True
       else:
           return False
print(bordo_zero_mat([[0, 0, 0, 0], [0, 7, 8, 0], [0, 0, 0, 0]]))
