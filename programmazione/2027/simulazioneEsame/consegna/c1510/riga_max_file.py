def riga_max_file(nomefile):
    f=open(nomefile,"r")
    contenuto=f.read()
    righe=f.splitlines()
    sommariga=0
    for i in l:
        sommariga+=righe[i]
    return sommariga
print(riga_max_file('riga_max_file2.txt'))      
        
        