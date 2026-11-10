class PriorityQueue:
    
    def __init__(self, data = None):
        '''builds an empty priority queue, or a priority queue containing all elements in list data. In the former case, list data itself is modified and used as a data container'''
        if data is None:
            self.__dim = 3  # length of the list, not necessarily equal to __n
            self.__heap = [None] * self.__dim
            self.__n = 1  # number of elements in the priority queue + 1
                          # element in position 0 is not used.
                          # __n is the first available position in __heap
        else: # data is assumed to be a list
            self.__dim = len(data)+1
            self.__heap = [None]  # starting dummy element
            self.__heap.extend(data)
            self.__n = self.__dim
            print(self)
            self.__make_heap()
        
    def is_empty(self):
        '''checks whether the priority queue is empty'''
        return self.__n == 1
    
    def insert(self, val):
        '''inserts a new element in the priority queue'''
        if self.__n == self.__dim: # double the list size, setting new elements to None
            self.__heap.extend([None] * self.__dim)
            self.__dim *= 2
        self.__heap[self.__n] = val # insert initially as last leaf
        pos = self.__n
        self.__n += 1
        while pos > 1 and self.__heap[pos//2] < val: # swap with parent while needed
            self.__heap[pos], self.__heap[pos//2] = self.__heap[pos//2], self.__heap[pos]
            pos = pos // 2
                
    def get_max(self):
        '''returns the maximum priority value in the heap'''
        if self.__n == 1:
            return None
        else:
            return self.__heap[1]
        
    def pop_max(self):
        '''returns and deletes the maximum priority value in the heap'''
        if self.__n == 1:
            return None
        else:
            max_val = self.__heap[1]
            self.__heap[1] = self.__heap[self.__n - 1] # move last leaf to the root
            self.__n -= 1
            self.__heapify(1) # recover parent-child condition
            return max_val
     
    def __heapify(self, pos):
        '''assuming the left and right subtrees of element pos are both heaps,
        recovers the heap condition for element pos and its subtree'''
        left_child = 2 * pos
        right_child = 2 * pos + 1
        largest = pos
        if left_child < self.__n and self.__heap[left_child] > self.__heap[largest]:
            largest = left_child
        if right_child < self.__n and self.__heap[right_child] > self.__heap[largest]:
            largest = right_child
        if largest != pos:
            self.__heap[pos], self.__heap[largest] = self.__heap[largest], self.__heap[pos]
            self.__heapify(largest)
                
    def __make_heap(self):   # O(n) worst-case time complexity heap construction
        last_parent = (self.__n - 1) // 2
        for p in range(last_parent, 0, -1):
            self.__heapify(p)
        
    def __str__(self):
        return f'{self.__n-1} elements: ' + str(self.__heap)

