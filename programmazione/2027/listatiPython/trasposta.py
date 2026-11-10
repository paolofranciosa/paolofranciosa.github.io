'''B, matrice trasposta di A
A n x m
B m x n

B[r,c] = A[c,r]

A come parametro, non modifica A, crea e restituisce B'''

def trasposta(A):
    '''crea e restituisce la matrice trasposta di A.
A lista di liste, verifichiamo che ogni lista abbia
la stessa lunghezza, accettiamo anche matrici di dimensione 0'''
    if len(A) == 0: # matrice vuota
        return [] # anche il risultato e' una matrice vuota
    # verifichiamo che tutte le righe abbiano la stessa lunghezza
    n = len(A)
    m = len(A[0])
    for r in range(1, n):
        if len(A[r]) != m:
            raise ValueError # termiona la funzione con una exception
    B = []
    # r indice di riga, c indice di colonna della matrice trasposta
    for r in range(m): # le m righe di B
        riga_della_trasposta = []
        for c in range(n):
            riga_della_trasposta.append(A[c][r])
        B.append(riga_della_trasposta)
    return B
     
if __name__ == "__main__":
#    mat = [[1,7,3], [4,0,2]]
    mat = [[1, 2, 3, 4]]
    print(mat)
    mat_T = trasposta(mat)
    print(mat_T)
print