from linkedListClassBis import LinkedList

l = LinkedList()    #  calls the constructor (   __init__
l.insert_front(10)  #   -> 10 is the head (last) element
l.insert_front(20)   #  20 is the head element, 10 is the next element
l.append(30)         #  -> 20 -> 10 -> 30 /
for x in l:
    print(x)