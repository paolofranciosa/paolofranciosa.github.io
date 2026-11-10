class PriorityQueue:
    '''implements a min priority queue, also allowing priority_decrease operation.
Each item consists in a list containing a key value and a priority value.
When creating a priority queue from data, data is a list of [keyval, priority] lists'''
    def __init__(self, data = None):
        self._address = dict() # stores position of each key value
        if data is None:
            self._dim = 3
            self._heap = [None] * self._dim
            self._n = 1  # element in position 0 is not used.
                         # _n is the first available position in _heap
        else:
            self._dim = len(data)+1
            self._heap = [None]  # starting dummy element
            self._heap.extend(data)
            self._n = self._dim
            for i in range(len(data)):
                self._address[data[i][0]] = i
            print(self)
            self._make_heap()
        
    def is_empty(self):
        return self._n == 1
    
    def contains(self, keyval):
        return keyval in self._address
        
    def insert(self, keyval, priority):
        '''If keyval does not exists it is inserted with its priority and returns True.
If keyval already exists and the new priority is less than its current priority, the priority is decreased to the new priority and returns True.
If keyval already exists and the new priority is not less than its current priority, the priority is not changed and returns False'''
        if not self.contains(keyval):
            if self._n == self._dim:
                self._heap.extend([None] * self._dim)
                self._dim *= 2
            self._address[keyval] = self._n
            self._heap[self._n] = [keyval, priority]
            self._n += 1
            self.decrease_priority(keyval, priority)
            return True
        elif priority < self._heap[self._address[keyval]][1]:
            self.decrease_priority(keyval, priority)
            return True
        else:
            return False
                
    def get_min(self):
        if self._n == 1:
            return None
        else:
            return self._heap[1]
        
    def pop_min(self):
        if self._n == 1:
            return None
        else:
            min_item = self._heap[1]
            self._heap[1] = self._heap[self._n - 1]
            self._address.pop(min_item[0])
            self._address[self._heap[1][0]] = 1
            self._n -= 1
            self._heapify(1)
            return min_item
    
    def decrease_priority(self, keyval, priority):
        pos = self._address[keyval]
        self._heap[pos][1] = priority
        while pos > 1 and self._heap[pos//2][1] > priority:
            self._heap[pos], self._heap[pos//2] = self._heap[pos//2], self._heap[pos]
            self._address[self._heap[pos][0]] = pos
            self._address[self._heap[pos//2][0]] = pos//2
            pos = pos // 2
        
        
    
    def _heapify(self, pos):
        left_child = 2 * pos
        right_child = 2 * pos + 1
        least = pos
        if left_child < self._n and self._heap[left_child][1] < self._heap[pos][1]:
            least = left_child
        if right_child < self._n and self._heap[right_child][1] < self._heap[least][1]:
            least = right_child
        if least != pos:
            self._heap[pos], self._heap[least] = self._heap[least], self._heap[pos]
            self._address[self._heap[pos][0]] = pos
            self._address[self._heap[least][0]] = least
            self._heapify(least)
                
    def _make_heap(self):   # O(n) worst-case time complexity
        last_parent = (self._n - 1) // 2
        for p in range(last_parent, 0, -1):
            self._heapify(p)
        
    def __str__(self):
        return f'{self._n-1} elements: ' + str(self._heap)

