from random import randint

def heap_sort(l):
    '''root is in position 0. So, children of i are 2i+1 and 2i+2,
while parent of i is (i-1)//2'''
    make_heap(l)
    print("heap:", l)
    for i in range(len(l)-1, 0, -1):  # len-1, len-2, ..., 3, 2, 1
        l[0], l[i] = l[i], l[0]     # swaps head (maximum in the heap portion) with last leaf
        heapify(l, 0, i)

def make_heap(l):
    last_parent = (len(l) - 2) // 2
    for p in range(last_parent, -1, -1):
        heapify(l, p)

def heapify(l, pos, end = None):
    '''l is a list, portion l[0:end] is a HEAP, portion l[end:] is increasingly sorted'''
    if end is None:
        end = len(l)
    swapped = True  # just for entering the while loop
    while swapped:
        swapped = False
        # also position 0 is used, so children are in positions 2*1 +1 and 2*1 + 2
        left_child = 2 * pos + 1
        right_child = 2 * pos + 2
        largest = pos
        if left_child < end and l[left_child] > l[pos]:
            largest = left_child
        if right_child < end and l[right_child] > l[largest]:
            largest = right_child
        if largest != pos:
            l[pos], l[largest] = l[largest], l[pos]
            pos = largest
            swapped = True

l = []
for i in range(20):
    l.append(randint(1, 100))
print("initial:", l)
heap_sort(l)
print("sorted: ", l)
