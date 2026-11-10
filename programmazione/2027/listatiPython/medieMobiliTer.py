def media(s):
    return sum(s)/len(s)

def medie_mobili(seq, k):
    medie = []
    for inizio in range(len(seq) - k + 1):
        medie.append(media(seq[inizio:inizio+k]))
    return medie
        

seq = [2, 4, 3, 6, 8, 9, 10, 12]  # len vale 8
k = 4   #inizio vale 0, 1, 2, 3, 4, 5 (è proprio 8-3),  5 compreso
m_mob = medie_mobili(seq, k)
print(m_mob)