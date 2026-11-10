def coppia_differenza_minima(L):
    '''La funzione riceve in input una lista contenente numeri.
Essa deve restituire un'altra lista contenente le due posizioni[i,j] dove
-i < j

-L[i] ed L[j] sono due elementi la cui differenza in valore assoluto
è minima rispetto ad ogni altra coppia di elementi in L.
la differenza minima può anche essere zero'''
    
    L = [-5,4,8,-3,1,3,10]
print(coppia_differenza_minima(L))
