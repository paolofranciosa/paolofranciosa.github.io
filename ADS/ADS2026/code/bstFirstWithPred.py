import random
import math

class BST:
    '''Implements a Binary Search Tree. Each node contains a key value and an info value,
    and a pair of references to left and right children.
    For simplifying the insert operation, the tree contains dummy leaves,
    with None value as key, for each missing child. Deletion is not implemented.
'''
    def __init__(self):
        '''creates an empty BST, consisting in a dummy leaf'''
        self.key = None
        self.info = None
        self.left = None
        self.right = None
#        self.num_elems = 0  # this can be updated during insertions and deletions
                             # in order to speed-up size() method
   
    def pred(self,x):
        '''returns the maximum element less than x, if it exists, None otherwise'''
        if self.key is None:
            return None
        elif x <= self.key:
            return self.left.pred(x)
        else:
            a = self.right.pred(x)
            if a is None:
                return self.key
            else:
                return a
        
    def insert(self, key, info):
        '''creates a new node containing key in the BST.
If key already exists, the previous info value is replaced by the current info
and returns False, otherwise a new node (with two dummy leaves)
is added and returns True'''
        if self.key is None:
            self.key = key
            self.info = info
            self.left = BST()
            self.right = BST()
            return True
        elif key < self.key:
            if self.left.insert(key, info):
                return True
            else:
                return False
        elif key > self.key:
            if self.right.insert(key, info):
                return True
            else:
                return False
        else: # key == self.key
            self.info = info
            return False

    def pre_order_visit(self):
        '''returns a list containing items in the BST according to an in-order visit'''
        if self.key is None:
            return []
        res = [(self.key, self.info)]
        res.extend(self.left.pre_order_visit())
        res.extend(self.right.pre_order_visit())
        return res
        
    def in_order_visit(self):
        '''returns a list containing items in the BST according to an in-order visit'''
        if self.key is None:
            return []
        res = self.left.in_order_visit()
        res.append((self.key, self.info))
        res.extend(self.right.in_order_visit())
        return res
        
    def post_order_visit(self):
        '''returns a list containing items in the BST according to an in-order visit'''
        if self.key is None:
            return []
        res = self.left.post_order_visit()
        res.extend(self.right.post_order_visit())
        res.append((self.key, self.info))
        return res
        
    def search(self, key):
        '''returns the value associated to key, if it exists.
Returns None if key does not exist'''
        if self.key is None: # search terminated in a dummy node
            return None
        elif key == self.key:
            return self.info
        elif key < self.key:
            return self.left.search(key)
        else:
            return self.right.search(key)

    def minimum(self):
        '''returns the pair key, info for the minimum key in the BST.
Returns None if the tree is empty'''
        # if the root has non left child, the root is the minimum
        # otherwise look in the left subtree
        
    def maximum(self):
        '''returns the pair key, info for the maximum key in the BST.
Returns None if the tree is empty'''
        # similar to minimum
                
    def height(self):
        if self.key is None:
            return 0
        else:
            return 1 + max(self.left.height(), self.right.height())

    def size(self):
        '''returns the number of elements in the tree'''
        # to be implemented recursively---see height()

    def print_tree(self):
        '''prints a parenthesized representation of the tree, similar to an in-order visit'''
        if self.key is not None:
            print("(", end="")
            self.left.print_tree()
            print(f' {self.key} ', end="")
            self.right.print_tree()
            print(")", end="")

if __name__ == "__main__":
    a = BST()
    items = [[23, 230], [12, 120], [44, 440], [11, 110], [10, 100], [13, 130], [40, 400], [45, 450], [42, 420]]
    for x in items:
        a.insert(x[0], x[1])
    
    a.print_tree()
    print()
    # print(f'size = {a.size()}')
    print("pre-order:", a.pre_order_visit())
    print("in-order:", a.in_order_visit())
    print("post-order:", a.post_order_visit())

#     l = a.in_order_visit()
#     for x in l:
#         print(f'key {x}: rank {a.rank(x[0])}')
    
#     print(f'minimum: {a.minimum()}')
#     print(f'maximum: {a.maximum()}')
#     
#     print("height:", a.height())
#     delete(22)
#     delete(30)
#     delete(45)
#     delete(44)
#     delete(23)
#     delete(12)
#     for x in items:
#         print(f'key {x[0]}: rank {a.rank(x[0])}')
#     
#     for i in range(a.size()):
#         print(a.get_kth_item(i))
#         
#     delete(10)
#     delete(11)
#     delete(40)
#     delete(13)
#     delete(42)
#     
#     num_keys = 10000000
#     max_val = 10 * num_keys
#     b = BST()
#     print(f'{"size":11s} {"h":4s}  {"log":4s}')
#     for i in range(num_keys):
#         x = random.randint(1, max_val)
#         b.insert(x, 111) # inserts (random_key, 111)
#         size = b.size()
#         if size in [2**k-1 for k in range(1,math.ceil(math.log2(num_keys)))]:
#             print(f'{size:9d} {b.height():4d}   {int(math.log2(size+1)):4d}')
#     print(f"built BST with {b.size()} keys. Height = {b.height()}")

    for x in range(8,50):
        print(f'pred({x}) = {a.pred(x)}')