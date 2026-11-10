def riga_max_file(nomefile):
    with open(nomefile, 'r') as f:
        d = f.read()
        h = d.splitlines()
        primovalore = 0
        segnariga = 0 
        valoriprova = 0
        for i in range(len(h)):
            K = h.split
            for n in K:
                valoriprova += n
        return valoriprova
             
 

print(riga_max_file('riga_max_file2.txt'))