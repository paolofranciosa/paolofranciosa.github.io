import time
import linkedListClass

def build_destroy_list(n, head=False):
    '''inserts n elements at the top or at the end of a Python list, then removes them.
Returns the number of seconds elapsed'''
    start = time.time()
    l = []
    if head:
        for i in range(n):
            l.insert(0, 25)
        for i in range(n):
            l.pop(0)
    else:
        for i in range(n):
            l.append(25)
        for i in range(n):
            l.pop()
    return time.time() - start

def build_destroy_linked_list(n):
    '''inserts n elements at the top of a linked list, thene removes them.
Returns the number of seconds elapsed'''
    start = time.time()
    l = linkedListClass.LinkedList()
    for i in range(n):
        l.insert_front(25)
    for i in range(n):
        l.remove_head()
    return time.time() - start

if __name__ == "__main__":
    n = 1000
    print(f"insertions   {'tail':10s}  {'head':10s}")
    while n <= 1000000:
        tail = build_destroy_list(n)
        print(f'{n:7d}  {tail:10.4f}', end="")
        head = build_destroy_list(n, True)
        print(f'  {head:10.4f}')
        n *= 2

    n = 1000
    print(f"insertions   linked list")
    while n <= 1000000:
        linked = build_destroy_linked_list(n)
        print(f'{n:7d}    {linked:10.4f}')
        n *= 2
