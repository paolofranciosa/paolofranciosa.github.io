seq = [3,5,1,8,4,2,5,7,6,3,4,1,9,8,4]

def seq_compresi(seq,x,y) :
    totale=0
    for n in seq: 
        if n >= x and n <= y:
            totale = totale+1
    return totale

n = seq_compresi(seq,3,5)
print(n)