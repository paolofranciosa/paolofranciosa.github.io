import random

class BinarySearchTree:
    '''implements a binary search tree. This is a "wrapper" class: a binary search tree
only contains a reference to a BST and the number of items in the BST.
TO BE MODIFIED, so that nodes of the BST contain both a "key" value and an "info" value.

Items are organized according to the "key" value

Insert operation has three parameters (self, key, info)

Search operation has only the (self, key) parameters,
and returns the "info" value associated to "key"

Delete operation has only (self, key) parameters'''
    def __init__(self):
        '''creates an empty binary search tree'''
        self._root = None
        self.size = 0
        
    def insert(self, key):
        '''inserts an item in the binary search tree. If key already exists it
is not inserted'''
        if self.search(key) is None:
            if self._root is None:
                self._root = BST(key)
            else:
                self._root.insert(key)
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
        '''deletes a key from the binary search tree, if key does exists'''
        if self._root is not None:
            self._root, exists = self._root.delete(key)
            # the second returned value is True iff key existed before deletion
        if exists:
            self.size -= 1
    
    def rank(self, key):
        '''TO BE WRITTEN: returns the number of keys in the binary search tree preceeding key.
E.g., rank(k) is 0 if k is the minimum key. If key does not exists None is returned.'''
        return 12345
        
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
        '''TO BE WRITTEN'''
        print('''print_tree MUST BE WRITTEN''')
        
class BST:
    def __init__(self, info):
        '''creates a BST consisting in a single node, with empty left and right subtrees'''
        self.key = info
        self.left = None
        self.right = None
        self.size = 1
        
    def insert(self, info):
        '''creates a new node in the BST containing key.
Is assumed that key does not already exist'''
        if info < self.key:
            if self.left is None:
                self.left = BST(info)
            else:
                self.left.insert(info)
        else:
            if self.right is None:
                self.right = BST(info)
            else:
                self.right.insert(info)
        self.size += 1

    def in_order_visit(self):
        '''returns a list containing items in the BST according to an in-order visit'''
        res = []
        if self.left is not None:
            res.extend(self.left.in_order_visit())
        res.append(self.key)
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
        res.append(self.key)
        return res
        
    def pre_order_visit(self):
        '''returns a list containing items in the BST according to a pre-order visit'''
        res = [self.key]
        if self.left is not None:
            res.extend(self.left.pre_order_visit())
        if self.right is not None:
            res.extend(self.right.pre_order_visit())
        return res
        
    def search(self, key):
        '''returns a pointer to the subtree whose root contains key, if it exists'''
        if key == self.key:
            return self
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
            return self.key
        else:
            return self.left.minimum()
        
    def maximum(self):
        '''returns the maximum key in the BST'''
        if self.right is None:
            return self.key
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
                self.key = self.right.minimum()          # copies successor in the root
                self.right, exists = self.right.delete(self.key) # deletes successor
                return self, True
            
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


def delete_and_print(x): # this method is just for showing deletions.
                         # It does not belong to the class
    a.delete(x)
    print(f"deleted {x}", a.in_order_visit(), end="")
    print(f' size = {a.get_size()}')

a = BinarySearchTree()
keys = [23, 12, 44, 11, 10, 13, 40, 45, 42]
for x in keys:
    a.insert(x)
a.print_tree()
print(f'size = {a.get_size()}')
print("pre-order:", a.pre_order_visit())
print("in-order:", a.in_order_visit())
print("post-order:", a.post_order_visit())

l = a.in_order_visit()
for x in l:
    print(f'key {x}: rank {a.rank(x)}')
print("height:", a.height())
delete_and_print(22)
delete_and_print(30)
delete_and_print(44)
delete_and_print(23)
delete_and_print(12)
for x in keys:
    print(f'key {x}: rank {a.rank(x)}')
delete_and_print(10)
delete_and_print(11)
delete_and_print(40)
delete_and_print(45)
delete_and_print(13)
delete_and_print(42)

numkeys = 1000000
b = BinarySearchTree()
for i in range(numkeys):
    b.insert(random.randint(1,10000000))
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