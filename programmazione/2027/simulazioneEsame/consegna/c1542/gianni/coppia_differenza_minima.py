import math
def coppia_differenza_minima(L):
    diff_min = abs(L[0] - L[1])
    scala = 1
    pos = [0, 1]
    for i in range(len(L) - 1):
        diff_corr = abs(L[scala] - L[i])
        if diff_corr < diff_min:
            pos[0] = scala
            pos[1] = i
        scala += 1
            
    if pos[0] > pos[1]:
        pos[0], pos[1] = pos[1], pos[0]
    
    return pos
        
        
seq = [-5,4,8,-3,1,3,10]
print(coppia_differenza_minima(seq))