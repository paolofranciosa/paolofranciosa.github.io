def tree(n):
    res = ''
    righe = 0
    while righe < n:
        colonne = 0
        while colonne < n:
            if colonne < n-righe-1:
                res = res + ' '
            else:
                res = res + '*'
            colonne = colonne + 1

        colonne = 0
        while colonne < righe:
            res = res + '*'
            colonne = colonne + 1
        res = res + '\n'
        righe = righe + 1
    
    return res
