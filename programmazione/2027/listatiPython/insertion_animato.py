def ins_sort(s):
    for i in range(1, len(s)):
        insert(s, i)
        
def insert(s, i):
    '''assumendo che s sia ordinata da [0] a [i-1],
inserisce l'elemento [i] creando una sequenza ordinata
da 0 a [i]'''
    x = s[i]
    pos = i
    while pos > 0 and s[pos - 1] > x:
        s[pos] = s[pos - 1]
        pos -= 1
    s[pos] = x
    stampa_sep(s, i)
    
def stampa_sep(s, i):
    '''stampa separatamente
il prefisso ordinato (fino a i compreso)
il suffisso non ordinato (da i+1 in poi)'''
    print(s[:i + 1], end = "    ")
    print(s[i + 1:])
    
seq = [5, 4, 2, 6, 4, 7, 9, 5, 6, 1, 3]
stampa_sep(seq, 0)
ins_sort(seq)