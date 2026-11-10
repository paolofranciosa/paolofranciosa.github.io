def riga_max_file(nomefile):
    with open(nomefile, "r") as f:
        contenuto = f.read()
        righe = contenuto.splitlines()
        massimo = 0
        sommaparti = sum(int(str(righe)).split())
        for i in righe:
            if parti > massimo:
                sommaparti = massimo
                rigamax = i
        return rigamax
            
print(riga_max_file("riga_max_file2.txt"))