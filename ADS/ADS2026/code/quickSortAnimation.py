'''run this code for seeing quick sort behaviour on a random sequence'''
import random

def quicksort(S, start=0, end=None):
    if end is None:
        end = len(S)-1
    if start > end:
        return
    if start == end:
        return
    pivot_pos = partition(S, start, end)
    print_list(s, start, pivot_pos, end, spazi = 4)
    quicksort(S, start, pivot_pos - 1)
    quicksort(S, pivot_pos+1, end)

def partition(S, start, end):
    # chose a random position for pivot
    pivot_pos = random.randint(start, end)
    pivot = S[pivot_pos]
    # swap pivot with head element
    S[start], S[pivot_pos] = S[pivot_pos], S[start]
    i = start+1
    j = end
    # scan list forwards from the start (pivot not included) towards center
    # and backwards from the end 
    while i<j:
        while i<j and S[i] < pivot: # look for element >= pivot
            i += 1
        while i<j and S[j] >= pivot: # look for element < pivot
            j -= 1
        if i<j:
            # swap the pair if found
            S[i], S[j] = S[j], S[i]
    if S[i] >= pivot: # decide whether pivot has to be put in position i or i-1
        i -= 1
    S[start], S[i] = S[i], S[start] # put the pivot in its final position
    return i
    
def random_list(n, maxval):
    s = [0] * n
    for i in range(len(s)):
        s[i] = random.randint(1, maxval)
    return s
    
def print_list(s, inizio = 0, pivot = 0, fine = None, spazi = 5):
    if fine is None:
        for i in range(len(s)):
            print(f"{s[i]:{spazi}d}", end = "")
        print()
    else:
        for i in range(pivot):
            print(f"{' ':{spazi}s}", end = "")
        print(f"({s[pivot]:{spazi-1}d})")
        
        for i in range(len(s)):
            if i < inizio or i == pivot or i > fine:
                print(f"{' ':{spazi}s}", end = "")
            else:
                print(f"{s[i]:{spazi}d}", end = "")
        print()
    
s = random_list(20, 99)
print_list(s, spazi = 4)
quicksort(s)
print_list(s, spazi = 4)
