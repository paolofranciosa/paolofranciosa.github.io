def bordo_zero_mat(M):
    conta=0
    for e in M:
        if conta==0 or conta==len(M)-1:
            for i in e:
                if i!=0:
                    return False
        else:
            if e[0]!=0 or e[len(e)-1]!=0:
                return False
        conta+=1
    return True
            
            
        
   
M1 = [[0]]
M2 = [[0,0,0,0], [0,7,8,0] , [0,0,0,0]]
M3 = [[1,0,0], [0,8,0] , [0,2,-1], [0,0,0]]
print(bordo_zero_mat(M1))
print(bordo_zero_mat(M2))
print(bordo_zero_mat(M3))       