def riga_max_file(nomefile) :
    massimo = 0
    indice1 = -1
    indice2 = 0
    f = open(nomefile, 'r')
    righe = f.readlines()
    for riga in righe :
        numeri_int = []
        numeri = riga.split()
        indice1 += 1
        for numero in numeri :
            numeri_int.append(int(numero))
            somma_f = sum(numeri_int)
            if somma_f > massimo:
                massimo = somma_f
                indice2 = indice1
    return indice2
                
            
            
    

print(riga_max_file('riga_max_file2.txt'))
            
            
                
    