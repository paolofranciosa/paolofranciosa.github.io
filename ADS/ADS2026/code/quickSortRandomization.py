import random

def quicksort(S, start=0, end=None):
    if end is None:
        end = len(S)-1
    if start>=end:
        return
    pivot_pos = partition(S, start, end)
    quicksort(S, start, pivot_pos - 1)
    quicksort(S, pivot_pos+1, end)

def partition(S, start, end):
    # choose pivot in random position
    pivot_pos = random.randint(start, end)
    pivot = S[pivot_pos]
    # swap pivot and start element
    S[start], S[pivot_pos] = S[pivot_pos], S[start]
    i = start+1
    j = end
    # scan list from the start (pivot excluded) towards the end
    # and from the end towards the start
    while i<j:
        while i<j and S[i] < pivot: # looks for an element >= pivot
            i += 1
        while i<j and S[j] >= pivot: # looks for an element < pivot
            j -= 1
        if i<j:
            # if a pair to be swapped is found 
            S[i], S[j] = S[j], S[i]
    if S[i] >= pivot: # decides whether pivot must go in position i or i-1
        i -= 1
    S[start], S[i] = S[i], S[start] # put pivot in the middle
    return i

example = [23, 21, 5, 2, 1, 55, 32, 67, 5, 67, 91, 12]
print("unsorted", example)
quicksort(example)
print("sorted  ", example)
