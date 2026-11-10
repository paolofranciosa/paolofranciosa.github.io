def riga_max_file(nomefile):
    righe = nomefile.splitlines()
    f = open("riga_max_file2.txt", "r", encoding = "utf8")
    return sum(righe) 

print(riga_max_file('riga_max_file2.txt'))