import random
        
class BST:
    def __init__(self, key=None, info=None):
        '''creates a BST consisting in a single node, whose left and right subtrees are
dummy nodes.
If key is None it is a dummy leaf'''
        self.key = key
        self.info = info
        if key is None: # creates a BST consisting only in a dummy node
            self.left = None
            self.right = None
            self.size = 0
        else: # creates a BST containing a single pair key, info
              # with two dummy BSTs as left and right subtrees
            self.left = BST() # 
            self.right = BST()
            self.size = 1
        
    def insert(self, key, info):
        '''creates a new node containing key in the BST.
If key already exists, the previous info value is replaced by the current info'''
        if self.key is None:
            self.key = key
            self.info = info
            self.left = BST()
            self.right = BST()
            self.size = 1
            return True
        elif key < self.key:
            if self.left.insert(key, info):
                self.size += 1
                return True
        elif key > self.key:
            if self.right.insert(key, info):
                self.size += 1
                return True
        else: # key == self.key
            self.info = info
            return False

    def pre_order_visit(self):
        '''returns a list containing items in the BST according to an in-order visit'''
        if self.key is None:
            return []
        res = [(self.key, self.info)]
        res.extend(self.left.in_order_visit())
        res.extend(self.right.in_order_visit())
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
        res = self.left.in_order_visit()
        res.extend(self.right.in_order_visit())
        res.append((self.key, self.info))
        return res
        
    def search(self, key):
        '''returns the value associated to key, if it exists'''
        if self.key is None: # search terminated in a dummy node
            return None
        elif key == self.key:
            return self.info
        elif key < self.key:
            return self.left.search(key)
        else:
            return self.right.search(key)

    def minimum(self):
        '''returns the pair key, info for the minimum key in the BST'''
        if self.left.key is None:
            return self.key, self.info
        else:
            return self.left.minimum()
        
    def maximum(self):
        '''returns the pair key, info for the maximum key in the BST'''
        if self.right.key is None:
            return self.key, self.info
        else:
            return self.right.maximum()
        
    def delete(self, key):
        '''deletes an item in the BST, if it exists'''
        if self.search(key) is not None: # checks wheter key exists
            if key == self.key and self.size == 1: # key is the only node in the BST
                                                   # BST is empty after deletion
                self.size = 0
                self.key = None
                self.info = None
                self.left = None
                self.right = None
            else:
                self = self.__eliminate(key) # calls a recursive deletion procedure
            
    def __eliminate(self, key):
        '''delets an item in the BST, if it exists'''
        self.size -= 1
        if key < self.key:
            self.left = self.left.__eliminate(key)
            return self
        elif key > self.key:
            self.right = self.right.__eliminate(key)
            return self
        else: # key == self.key
            if self.left.key is None:
                return self.right
            elif self.right.key is None:
                return self.left
            else:
                self.key, self.info = self.right.minimum()
                self.right = self.right.__eliminate(self.key)
                return self
    
    def rank(self, key):
        if self.search(key) is None:
            return None
        else:
            return self._compute_rank(key)
        
    def _compute_rank(self, key):
        if key < self.key:
            return self.left._compute_rank(key)
        elif key == self.key:
            return self.left.size
        else:
            return self.left.size + 1 + self.right._compute_rank(key)

    def get_kth_item(self, rank):
        '''returns key and info for the item having a given rank.
It is assumed rank >= 0 and rank < size'''
        if rank < self.left.size:
            return self.left.get_kth_item(rank)
        elif rank == self.left.size:
            return self.key, self.info
        else:
            return self.right.get_kth_item(rank-self.left.size-1)
        
    def height(self):
        if self.key is None:
            return 0
        else:
            return 1 + max(self.left.height(), self.right.height())

    def get_size(self):
        return self.size

    def print_tree(self):
        '''prints a parenthesized representation of the tree, similar to an in-order visit'''
        if self.key is not None:
            print("(", end="")
            self.left.print_tree()
            print(f' {self.key} ', end="")
            self.right.print_tree()
            print(")", end="")


def delete_and_print(x): # this method is just for showing deletion process.
                         # It does not belong to the class
    a.delete(x)
    print(f"deleted {x} ", end="")
    a.print_tree()
    print(f' size = {a.get_size()}')
    print(f' height = {a.height()}')


a = BST()

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

for i in range(a.get_size()):
    print(a.get_kth_item(i))
    
delete_and_print(10)
delete_and_print(11)
delete_and_print(40)
delete_and_print(13)
delete_and_print(42)

numkeys = 1000000
b = BST()
for i in range(numkeys):
    x = random.randint(1,10000000)
    b.insert(x, 111)
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