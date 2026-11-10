from random import *
from priority import PriorityQueue
    
h = PriorityQueue()
h.insert(45)
h.insert(12)
h.insert(23)
h.insert(84)
h.insert(74)
print(f'topped {h.pop_max()}')
h.insert(34)
h.insert(85)
h.insert(1)
print(f'topped {h.pop_max()}')
print(f'topped {h.pop_max()}')
h.insert(28)
h.insert(63)
h.insert(163)
h.insert(62)
print(h)
while not h.is_empty():
    print(h.pop_max())

l = []
for i in range(20):
    l.append(randint(1, 100))
print(l)
heap = PriorityQueue(l)
print(heap)
while not heap.is_empty():
    print(heap.pop_max())

