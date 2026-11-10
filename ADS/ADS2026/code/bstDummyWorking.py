import random
import math

class BST:
    def __init__(self):
        '''creates an empty BST, consisting in a dummy leaf'''
        self.__key = None
        self.__info = None
        self.__left = None
        self.__right = None
        self.__num_elems = 0   # maintains the number of nodes (dummy excluded) in each subtree
        
    def insert(self, key, info):
        '''creates a new node containing key in the BST.
If key already exists, the previous info value is replaced by the current info and returns False, otherwise a new node (with two dummy leaves) is added and returns True'''
        if self.__key is None:
            self.__key = key
            self.__info = info
            self.__left = BST()
            self.__right = BST()
            self.__num_elems = 1
            return True
        elif key < self.__key:
            if self.__left.insert(key, info):
                self.__num_elems += 1
                return True
            else:
                return False
        elif key > self.__key:
            if self.__right.insert(key, info):
                self.__num_elems += 1
                return True
            else:
                return False
        else: # key == self.__key
            self.__info = info
            return False

    def pre_order_visit(self):
        '''returns a list containing items in the BST according to an in-order visit'''
        if self.__key is None:
            return []
        res = [(self.__key, self.__info)]
        res.extend(self.__left.pre_order_visit())
        res.extend(self.__right.pre_order_visit())
        return res
        
    def in_order_visit(self):
        '''returns a list containing items in the BST according to an in-order visit'''
        if self.__key is None:
            return []
        res = self.__left.in_order_visit()
        res.append((self.__key, self.__info))
        res.extend(self.__right.in_order_visit())
        return res
        
    def post_order_visit(self):
        '''returns a list containing items in the BST according to an in-order visit'''
        if self.__key is None:
            return []
        res = self.__left.post_order_visit()
        res.extend(self.__right.post_order_visit())
        res.append((self.__key, self.__info))
        return res
        
    def search(self, key):
        '''returns the value associated to key, if it exists.
Returns None if key does not exist'''
        if self.__key is None: # search terminated in a dummy node
            return None
        elif key == self.__key:
            return self.__info
        elif key < self.__key:
            return self.__left.search(key)
        else:
            return self.__right.search(key)

    def minimum(self):
        '''returns the pair key, info for the minimum key in the BST.
Returns None if the tree is empty'''
        if self.__left.__key is None:
            return self.__key, self.__info
        else:
            return self.__left.minimum()
        
    def maximum(self):
        '''returns the pair key, info for the maximum key in the BST.
Returns None if the tree is empty'''
        if self.__right.__key is None:
            return self.__key, self.__info
        else:
            return self.__right.maximum()
        
    def delete(self, key):
        '''deletes an item in the BST, if it exists'''
        if self.search(key) is not None: # checks whether key exists
            if key == self.__key and self.size() == 1: # key is the only node in the BST
                                                   # BST is empty after deletion
                self.__num_elems = 0
                self.__key = None
                self.__info = None
                self.__left = None
                self.__right = None
            else:
                self = self.__eliminate(key) # calls a recursive deletion procedure
            
    def __eliminate(self, key):
        '''deletes an item in the BST, if it exists'''
        self.__num_elems -= 1
        if key < self.__key:
            self.__left = self.__left.__eliminate(key)
            return self
        elif key > self.__key:
            self.__right = self.__right.__eliminate(key)
            return self
        else: # key == self.__key
            if self.__left.__key is None:
                return self.__right
            elif self.__right.__key is None:
                return self.__left
            else:
                self.__key, self.__info = self.__right.minimum()
                self.__right = self.__right.__eliminate(self.__key)
                return self
    
    def rank(self, key):
        if self.search(key) is None:
            return None
        else:
            return self._compute_rank(key)
        
    def _compute_rank(self, key):
        if key < self.__key:
            return self.__left._compute_rank(key)
        elif key == self.__key:
            return self.__left.__num_elems
        else:
            return self.__left.__num_elems + 1 + self.__right._compute_rank(key)

    def get_kth_item(self, rank):
        '''returns key and info for the item having a given rank.
It is assumed rank >= 0 and rank < size'''
        if rank < self.__left.__num_elems:
            return self.__left.get_kth_item(rank)
        elif rank == self.__left.__num_elems:
            return self.__key, self.__info
        else:
            return self.__right.get_kth_item(rank-self.__left.__num_elems-1)
        
    def height(self):
        if self.__key is None:
            return 0
        else:
            return 1 + max(self.__left.height(), self.__right.height())

    def size(self):
        return self.__num_elems

    def print_tree(self):
        '''prints a parenthesized representation of the tree, similar to an in-order visit'''
        if self.__key is not None:
            print("(", end="")
            self.__left.print_tree()
            print(f' {self.__key} ', end="")
            self.__right.print_tree()
            print(")", end="")


def delete_and_print(x): # this method is just for showing deletion process.
                         # It does not belong to the class
    a.delete(x)
    print(f"deleted {x} ", end="")
    a.print_tree()
    print(f' size = {a.size()}')
    print(f' height = {a.height()}')


a = BST()

items = [[23, 230], [12, 120], [44, 440], [11, 110], [10, 100], [13, 130], [40, 400], [45, 450], [42, 420]]
for x in items:
    a.insert(*x)

a.print_tree()
print(f'size = {a.size()}')
print("pre-order:", a.pre_order_visit())
print("in-order:", a.in_order_visit())
print("post-order:", a.post_order_visit())

l = a.in_order_visit()
for x in l:
    print(f'key {x}: rank {a.rank(x[0])}')

print(f'minimum: {a.minimum()}')
print(f'maximum: {a.maximum()}')

print("height:", a.height())
delete_and_print(22)
delete_and_print(30)
delete_and_print(45)
delete_and_print(44)
delete_and_print(23)
delete_and_print(12)
for x in items:
    print(f'key {x[0]}: rank {a.rank(x[0])}')

for i in range(a.size()):
    print(a.get_kth_item(i))
    
delete_and_print(10)
delete_and_print(11)
delete_and_print(40)
delete_and_print(13)
delete_and_print(42)
print(a.search(42))
delete_and_print(42)

num_keys = 100000
max_val = 10 * num_keys
b = BST()
print(f'{"size":11s} {"h":4s}  {"log":4s}')
for i in range(num_keys):
    x = random.randint(1, max_val)
    b.insert(x, 111) # inserts (random_key, 111)
    size = b.size()
    if size in [2**k-1 for k in range(1,math.ceil(math.log2(num_keys)))]:
        print(f'{size:9d} {b.height():4d}   {int(math.log2(size+1)):4d}')
print(f"built BST with {b.size()} keys. Height = {b.height()}")

#x = int(input("type a number (0 to stop)"))
#while x != 0:
#    n = a.search(x)
#    if n is None:
#        print(x, "does not exist")
#    else:
#        print(n.key)
#    x = int(input("type a number (0 to stop)"))