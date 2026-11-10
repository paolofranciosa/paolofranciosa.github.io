def bubblesort(seq):
    for end in range(len(seq)-1, 0, -1):
        scambio = False
        for j in range(end):
            if seq[j] > seq[j+1]:
                scambio = True
                seq[j], seq[j+1] = seq[j+1], seq[j]
        if not scambio:
            return

l = [5, 3, 2, 6, 7, 5, 4, 7, 9, 1, 3]
print(l)
bubblesort(l)
print(l)