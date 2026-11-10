def seq_compresi(L, low, high):
    numero_valori=0
    for i in L:
         if i<=high and i>=low:
             numero_valori+=1
    return numero_valori
seq = [3,5,1,8,4,2,5,7,6,3,4,1,9,8,4]
n = seq_compresi(seq,3,5)
print(n)
