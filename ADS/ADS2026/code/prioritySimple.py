class PriorityQueue:
    '''implements a priority queue. Only priority values are inserted/retrieved,
a useful implementation should associate an "info" value to each priority while inserting, and
retrieveng the pair "priority, info" with maximum priority'''
    def __init__(self):
        '''builds an empty heap'''
        self.__dim = 3  # initial dimension of the heap
        self.__heap = [None] * self.__dim  # builds a list containing self.__dim items, all set to None
        self.__n = 1  # number of elements currently used in the heap (minus 1)
                     # element in position 0 is not used.
                     # __n is the first available position in __heap
        
    def is_empty(self):
        '''returns True if and only if the PriorityQueue contains no elements'''
        return self.__n == 1
    
    def insert(self, val):
        '''inserts a new priority value in the heap'''
        if self.__n == self.__dim: # if necessary, the heap is doubled appending None elements
            self.__heap.extend([None] * self.__dim)
            self.__dim *= 2
        self.__heap[self.__n] = val # new item is initially put at the end
        pos = self.__n
        self.__n += 1
        while pos > 1 and self.__heap[pos//2] < val: # swap with the parent if needed
            self.__heap[pos], self.__heap[pos//2] = self.__heap[pos//2], self.__heap[pos]
            pos = pos // 2
                
    def get_max(self):
        '''returns the maximum priority in the heap, None if it is empty'''
        if self.__n == 1:
            return None
        else:
            return self.__heap[1]
        
    def pop_max(self):
        '''removes the maximum priority from the heap, and returns its value.
Returns None if teh heap is empty'''
        if self.__n == 1:
            return None
        else:
            max_val = self.__heap[1]
            self.__heap[1] = self.__heap[self.__n - 1]
            self.__n -= 1
            self.__heapify(1) # solve the possible violation in position 1
            return max_val
     
    def __heapify(self, pos):
        '''checks whether element in position "pos" is not greater that both children,
and swaps with the largest children'''
        left_child = 2 * pos
        right_child = 2 * pos + 1
        largest = pos
        if left_child < self.__n and self.__heap[left_child] > self.__heap[pos]:
            largest = left_child
        if right_child < self.__n and self.__heap[right_child] > max(self.__heap[left_child], self.__heap[pos]):
            largest = right_child
        if largest != pos:
            self.__heap[pos], self.__heap[largest] = self.__heap[largest], self.__heap[pos]
            self.__heapify(largest)  # if a swap occurred, the child's position is recurseively checked
                
    def __str__(self):
        return f'{self.__n-1} elements: ' + str(self.__heap)

