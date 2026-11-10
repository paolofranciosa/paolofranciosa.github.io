import random

class BinarySearchTree:
    '''implements a binary search tree. This is a "wrapper" class: a binary search tree
only contains a reference to a BST and the number of items in the BST'''
    def __init__(self):
        '''creates an empty binary search tree'''
        self._root = None
        self.size = 0
        
    def insert(self, key, info):
        '''inserts an item in the binary search tree. If key already exists it
is not inserted'''
        if self.search(key) is None:
            if self._root is None:
                self._root = BST(key, info)
            else:
                self._root.insert(key, info)
            self.size += 1
    
    def search(self, key):
        '''returns a reference to the item containing key, if it exists'''
        if self._root is None:
            return None
        else:
            return self._root.search(key)
        
    def in_order_visit(self):
        '''returns a list containing keys in the binary search tree,
according to an in-order visit'''
        if self._root is None:
            return None
        else:
            return self._root.in_order_visit()

    def post_order_visit(self):
        '''returns a list containing keys in the binary search tree,
according to a post-order visit'''
        if self._root is None:
            return None
        else:
            return self._root.post_order_visit()

    def pre_order_visit(self):
        '''returns a list containing keys in the binary search tree,
according to a pre-order visit'''
        if self._root is None:
            return None
        else:
            return self._root.pre_order_visit()

    def minimum(self):
        '''returns the minimum key in the binary search tree.
If the BST is empty it returns None'''
        if self._root is None:
            return None
        else:
            return self._root.minimum()
        
    def maximum(self):
        '''returns the maximum key in the binary search tree.
If the BST is empty it returns None'''
        if self._root is None:
            return None
        else:
            return self._root.maximum()
        
    def delete(self, key):
        '''deletes an item from the binary search tree, if key does exists'''
        if self._root is not None:
            self._root, exists = self._root.delete(key)
            # the second returned value is True iff key existed before deletion
        if exists:
            self.size -= 1
    
    def rank(self, key):
        '''returns the number of keys in the binary search tree preceeding key.
E.g., rank(k) is 0 if k is the minimum key. If key does not exists None is returned.'''
        if self._root is None:
            return None
        elif self.search(key) is None:
            return None
        else:
            return self._root.rank(key)
        
    def get_kth_item(self, rank):
        '''returns key and info for the item having a given rank.
If rank < 0 or rank >= size returns None, None'''
        if rank < 0 or rank >= self.size:
            return None, None
        else:
            return self._root.get_kth_item(rank)
    
    def height(self):
        '''returns the number of levels in the binary search tree.
Height is 1 if the binary search tree contains only the root'''
        if self._root is None:
            return 0
        else:
            return self._root.height()
    
    def get_size(self):
        '''returns the number of keys in the binary search tree'''
        return self.size
        
    def print_tree(self):
        if self._root is None:
            print("()")
        else:
            self._root.print_tree()
            print()
        
class BST:
    def __init__(self, k, i):
        '''creates a BST consisting in a single node, with empty left and right subtrees'''
        self.key = k
        self.info = i
        self.left = None
        self.right = None
        self.size = 1
        
    def insert(self, k, i):
        '''creates a new node in the BST containing key.
Is assumed that key does not already exist'''
        if k < self.key:
            if self.left is None:
                self.left = BST(k, i)
            else:
                self.left.insert(k, i)
        else:
            if self.right is None:
                self.right = BST(k, i)
            else:
                self.right.insert(k, i)
        self.size += 1

    def in_order_visit(self):
        '''returns a list containing items in the BST according to an in-order visit'''
        res = []
        if self.left is not None:
            res.extend(self.left.in_order_visit())
        res.append((self.key, self.info))
        if self.right is not None:
            res.extend(self.right.in_order_visit())
        return res
        
    def post_order_visit(self):
        '''returns a list containing items in the BST according to a post-order visit'''
        res = []
        if self.left is not None:
            res.extend(self.left.post_order_visit())
        if self.right is not None:
            res.extend(self.right.post_order_visit())
        res.append((self.key, self.info))
        return res
        
    def pre_order_visit(self):
        '''returns a list containing items in the BST according to a pre-order visit'''
        res = [(self.key, self.info)]
        if self.left is not None:
            res.extend(self.left.pre_order_visit())
        if self.right is not None:
            res.extend(self.right.pre_order_visit())
        return res
        
    def search(self, key):
        '''returns a pointer to the subtree whose root contains key, if it exists'''
        if key == self.key:
            return self.info
        elif key < self.key:
            if self.left is None:
                return None
            else:
                return self.left.search(key)
        else:
            if self.right is None:
                return None
            else:
                return self.right.search(key)

    def minimum(self):
        '''returns the minimum key in the BST'''
        if self.left is None:
            return self.key, self.info
        else:
            return self.left.minimum()
        
    def maximum(self):
        '''returns the maximum key in the BST'''
        if self.right is None:
            return self.key, self.info
        else:
            return self.right.maximum()
        
    def delete(self, key):
        if key < self.key:
            if self.left is None:
                return self, False
            else:
                self.left, exists = self.left.delete(key)
                if exists:
                    self.size -= 1
                return self, exists
        elif key > self.key:
            if self.right is None:
                return self, False
            else:
                self.right, exists = self.right.delete(key)
                if exists:
                    self.size -= 1
                return self, exists
        else: # key == self.key
            if self.left is None:
                return self.right, True
            elif self.right is None:
                return self.left, True
            else:
                self.size -= 1
                self.key, self.info = self.right.minimum()          # copies successor in the root
                self.right, exists = self.right.delete(self.key) # deletes successor
                return self, True
    
    def rank(self, key):
        if key < self.key:
            return self.left.rank(key)
        else:
            if self.left is None:
                left_size = 0
            else:
                left_size = self.left.size
            if key == self.key:
                return left_size
            else:
                return left_size + 1 + self.right.rank(key)

    def get_kth_item(self, rank):
        '''returns key and info for the item having a given rank.
It is assumed rank >= 0 and rank < size'''
        if self.left is None:
            left_size = 0
        else:
            left_size = self.left.size
        if rank < left_size:
            return self.left.get_kth_item(rank)
        elif rank == left_size:
            return self.key, self.info
        else:
            return self.right.get_kth_item(rank-left_size-1)
        
    def height(self):
        if self.left is None:
            left_height = 0
        else:
            left_height = self.left.height()
        if self.right is None:
            right_height = 0
        else:
            right_height = self.right.height()
        return 1 + max(left_height, right_height)

    def get_size(self):
        return self.size

    def print_tree(self):
        print("(", end="")
        if self.left is not None:
            self.left.print_tree()
        print(f' {self.key} ', end="")
        if self.right is not None:
            self.right.print_tree()
        print(")", end="")


def delete_and_print(x): # this method is just for showing deletions.
                         # It does not belong to the class
    a.delete(x)
    print(f"deleted {x}", a.in_order_visit(), end="")
    print(f' size = {a.get_size()}')

a = BinarySearchTree()
items = [[23, 230], [12, 120], [44, 440], [11, 110], [10, 100], [13, 130], [40, 400], [45, 450], [42, 420]]
for x in items:
    a.insert(*x)
a.print_tree()
print(f'size = {a.get_size()}')
print("pre-order:", a.pre_order_visit())
print("in-order:", a.in_order_visit())
print("post-order:", a.post_order_visit())

l = a.in_order_visit()
for x in l:
    print(f'key {x}: rank {a.rank(x[0])}')
print("height:", a.height())
delete_and_print(22)
delete_and_print(30)
delete_and_print(44)
delete_and_print(23)
delete_and_print(12)
for x in items:
    print(f'key {x[0]}: rank {a.rank(x[0])}')

for i in range(a.get_size()):
    print(a.get_kth_item(i))
    
delete_and_print(10)
delete_and_print(11)
delete_and_print(40)
delete_and_print(45)
delete_and_print(13)
delete_and_print(42)

numkeys = 1000000
b = BinarySearchTree()
for i in range(numkeys):
    b.insert(random.randint(1,10000000), 111)
# print(b.in_order_visit())
print(f"built BST with {numkeys} keys:")
print(f"height: {b.height()}")
print(f"actual size (unique key values): {b.get_size()}")

#x = int(input("type a number (0 to stop)"))
#while x != 0:
#    n = a.search(x)
#    if n is None:
#        print(x, "does not exist")
#    else:
#        print(n.key)
#    x = int(input("type a number (0 to stop)"))