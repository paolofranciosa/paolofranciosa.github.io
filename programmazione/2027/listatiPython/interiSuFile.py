def scrivi_interi(nome_file, n):
    '''crea un file di testo di nome nome_file (str) che contiene gli
interi da 0 a n-1, uno per riga
'''
    f = open(nome_file, "w", encoding="utf-8")
    for i in range(n):
        print(i, file = f) # invece che su schermo, scrive nel file f
#        f.write(str(i)+"\n")
    f.close()
    
    
scrivi_interi("pippo.txt", 10)