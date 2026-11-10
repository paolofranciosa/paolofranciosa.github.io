# complessità O(n)
def medie_mobili(seq, k):
    somma = 0
    for i in range(k):
        somma += seq[i]
    medie = [somma/k]
    for inizio in range(0, len(seq)-k):
        # modificare somma
        somma -= seq[inizio]
        somma += seq[inizio+k]
        medie.append(somma/k)
    return medie
      
seq = [2, 4, 3, 6, 8, 9, 10, 12]  # len vale 8
k = 4   #inizio vale 0, 1, 2, 3, 4, 5 (è proprio 8-3),  5 compreso
m_mob = medie_mobili(seq, k)
print(m_mob)