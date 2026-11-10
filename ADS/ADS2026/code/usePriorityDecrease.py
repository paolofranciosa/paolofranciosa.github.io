from random import *
from priorityDecrease import PriorityQueue
    
h = PriorityQueue()
h.insert("45",45)
h.insert("12",12)
h.insert("23",23)
h.insert("84",84)
h.insert("74",74)
#print(f'topped {h.pop_min()}')
h.insert("34",34)
h.insert("85",85)
h.insert("1",1)
#print(f'topped {h.pop_min()}')
#print(f'topped {h.pop_min()}')
h.insert("28",28)
h.insert("63",63)
h.insert("163",163)
h.insert("62",62)
h.decrease_priority("63", 10)
h.decrease_priority("163", 2)
print(h)
while not h.is_empty():
    print(h.pop_min())

l = []
for i in range(20):
    p = randint(1, 100)
    l.append([str(p), p])
print(l)
heap = PriorityQueue(l)
print(heap)
while not heap.is_empty():
    print(heap.pop_min())

