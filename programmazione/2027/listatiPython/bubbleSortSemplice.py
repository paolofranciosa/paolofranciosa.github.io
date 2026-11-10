import random

def stupid_bubblesort(seq):
     # end is the last position in the non-ordered portion
    for end in range(len(seq)-1, 0, -1):
        for j in range(end):
            print(f'confronto {j} {j+1}')
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
                
if __name__ == "__main__":
    a = [None] * 5
    for i in range(len(a)):
        a[i] = random.randint(1, 99)
    print(a)
    stupid_bubblesort(a)
    print(a)