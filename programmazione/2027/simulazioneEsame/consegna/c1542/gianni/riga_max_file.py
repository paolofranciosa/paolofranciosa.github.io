def riga_max_file(nomefile):
    with open(nomefile, 'r', encoding= 'utf-8') as file:
        prima = file.readline()
        num = prima.split()
        max_somma = 0
        for n in num:
            max_somma += int(n)
        
        indice_max = 0
        indice_corrente = 1
        
        for riga in file:
            numeri = riga.split()
            somma = 0
            for n in numeri:
                somma += int(n)
            if somma > max_somma:
                max_somma = somma
                indice_max = indice_corrente
                indice_corrente += 1
        return indice_max
        
    
print(riga_max_file('riga_max_file2.txt'))
                
                
                