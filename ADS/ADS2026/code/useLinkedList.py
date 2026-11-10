from linkedListClass import LinkedList

l = LinkedList()    #  calls the constructor   __init__
print("lenght:", l.get_len())
l.insert_front(10)  #   -> 10 is the head (last) element
l.insert_front(20)   #  20 is the head element, 10 is the next element
l.append(30)         #  -> 20 -> 10 -> 30 /
# l.insert_after(10, 15)   # 20 -> 10 -> 15 -> 30 /
l.append(4)
# l.insert_after(4, 444)   #  -> 20 -> 10 -> 15 -> 30 -> 4 -> 444
print("lenght:", l.get_len())
print(l.get_list())  #  returns [20, 10, 15, 30, 4, 444]
a = LinkedList()
a.insert_front(111)
a.insert_front(222)
a.append(333)
l.concatenate(a)
y = LinkedList()
y.concatenate(a)
print(y.get_list())
print(y.get_head())
print(l.get_list())
l.remove_val(20)
print(l.get_list())
l.remove_val(4)
print(l.get_list())
l.remove_val(10)
print(l.get_list())
print("contains(30):", l.contains(30))
print("contains(15):", l.contains(15))
print("contains(4):", l.contains(4))
print("contains(35):", l.contains(35))
print("contains(10):", l.contains(10))
l.remove_head()
print(l.get_list())
print(l.get_head())

