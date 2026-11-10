def riga_max_file(nomefile):
    with open(nomefile) as pippo:
        gigio = pippo.readlines()
        rigamax = 0
        n = 0
        rigavalmax = 0
        for i in gigio:
            n += 1
            lista = i.split()
            lista1 = []
            for i in lista:
                lista1.append(int(i))
            luigi = sum(lista1)
            if luigi > rigavalmax:
                rigavalmax = luigi
                rigamax = n
        return (rigamax-1)
            
print(riga_max_file("riga_max_file1.txt"))