def sort(s): # sort the whole sequence, the result is s itself
    merge_sort(s, 0, len(s)-1)  # ask to sort the interval of s from 0 to len - 1
    return
    
def merge_sort(s, start, end):  # works on interval from start to end (both included)
    '''merge sort algorithm, O(n log n)'''
    if start < end: # we are not in the base case
        mid = (start + end) // 2
        merge_sort(s, start, mid)
        merge_sort(s, mid+1, end)
        merge(s, start, mid, end)  # merge, fist part in [start, mid] second part in [mid+1, end]
    return

def merge(s, start, mid, end):
    # define a new sequence, in which we put the merging elements one at the time in the correct order
    temp = []  #initially empty
    i = start # used to scan the first portion
    j = mid+1 # used to scan the second portion
    while i <= mid and j <= end: # as long as there are elements to take in both portions
        # take the minimum and put in into temp
        if s[i] <= s[j]:  # take from the first portion
            temp.append(s[i])
            i += 1
        else:             # take from the second portion
            temp.append(s[j])
            j += 1
    # check which is the remaining portion tail
    if i > mid: # tail is in the second portion, from j to end  (included)
        for k in range(j, end+1):
            temp.append(s[k])
    else:       # tail is in the first portion, from i to mid (included)
        for k in range(i, mid+1):
            temp.append(s[k])
    # copy the temp sequence back in the correct portion of s
    # shifting by "start" positions
    for p in range(len(temp)):  # 0, 1, 2, ...
        s[start+p] = temp[p]
    return
        

s = [543, 23, 1, 66, 132, 45, 1, 1, 66, 23] #  stable sort  if  ->   ..., 23a, 23b, ...
print(s)  # prints the initial sequence
sort(s)
print(s)  # prints s after it has been sorted