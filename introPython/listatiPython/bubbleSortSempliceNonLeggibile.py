def stupid_bubblesort(seq):
    for i in range(1,len(seq)):
        for j in range(0,len(seq)-i):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]