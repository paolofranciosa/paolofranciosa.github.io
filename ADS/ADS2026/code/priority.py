class PriorityQueue:
    
    def __init__(self, data = None):
        '''builds an empty priority queue, or a priority queue containing all elements in list data. In the former case, list data itself is modified and used as a data container.
The root is in position 1, children of element in position i are in positions 2*i and 2*i+1'''
        if data is None:
            self.__heap = [None]
        else: # data is assumed to be a list
            self.__heap = [None] # starting dummy element
            self.__heap.extend(data)
#            print(self)
            self.__make_heap()
        
    def is_empty(self):
        '''checks whether the priority queue is empty'''
        return len(self.__heap) == 1
    
    def insert(self, val):
        '''inserts a new element in the priority queue'''
        self.__heap.append(val) # insert initially as last leaf
        pos = len(self.__heap) - 1
        while pos > 1 and self.__heap[pos//2] < val: # swap with parent while needed
            self.__heap[pos], self.__heap[pos//2] = self.__heap[pos//2], self.__heap[pos]
            pos = pos // 2
                
    def get_max(self):
        '''returns the maximum priority value in the heap'''
        if len(self.__heap) == 1:
            return None
        else:
            return self.__heap[1]
        
    def pop_max(self):
        '''returns and deletes the maximum priority value in the heap'''
        if len(self.__heap) == 1:
            return None
        else:
            max_val = self.__heap[1]
            self.__heap[1] = self.__heap[-1] # move last leaf to the root
            self.__heap.pop()
            self.__heapify(1) # recover parent-child condition
            return max_val
     
    def __heapify(self, pos):
        '''assuming the left and right subtrees of element pos are both heaps,
        recovers the heap condition for element pos and its subtree'''
        left_child = 2 * pos
        right_child = 2 * pos + 1
        largest = pos
        last_pos = len(self.__heap)
        if left_child < last_pos and self.__heap[left_child] > self.__heap[largest]:
            largest = left_child
        if right_child < last_pos and self.__heap[right_child] > self.__heap[largest]:
            largest = right_child
        if largest != pos:
            self.__heap[pos], self.__heap[largest] = self.__heap[largest], self.__heap[pos]
            self.__heapify(largest)
                
    def __make_heap(self):   # O(n) worst-case time complexity heap construction
                            # starting from a list containing arbitrary elements
        last_parent_pos = (len(self.__heap) - 1) // 2
        print(f'last_parent_pos: {last_parent_pos}, element {self.__heap[last_parent_pos]}')
        for p in range(last_parent_pos, 0, -1):
            self.__heapify(p)
        
    def __str__(self):
        return f'{len(self.__heap)-1} elements: ' + str(self.__heap)

