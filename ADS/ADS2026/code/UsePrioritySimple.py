from random import *
from prioritySimple import PriorityQueue
    
h = PriorityQueue()
h.insert(45)
h.insert(12)
h.insert(23)
h.insert(84)
h.insert(74)
print(f'topped {h.pop_max()}') # 84
h.insert(34)
h.insert(85)
h.insert(1)
print(f'topped {h.pop_max()}')  # 85
print(f'topped {h.pop_max()}')  # 74
h.insert(28)
h.insert(63)
h.insert(163)
h.insert(62)
print(h)
while not h.is_empty():
    print(h.pop_max())


