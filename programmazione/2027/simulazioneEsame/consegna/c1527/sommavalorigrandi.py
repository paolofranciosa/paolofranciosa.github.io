def sommavalorigrandi (d, soglia):
    a=0
    #b=[]
    for chiave in d:
        #b.append(chiave)
    #for i in range (b)):
        if d[chiave]>soglia:
            a+=d[chiave]
    return a
print(sommavalorigrandi({'xx': 44, 'yy': 33, 'zz': 22, 'qw': 22, 'das': 11}, 20))