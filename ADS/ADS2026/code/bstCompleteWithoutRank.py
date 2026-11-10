class BST:
    def __init__(self):
        '''creates an empty BST, consisting in a single dummy leaf'''
        self.__key = None
        self.__info = None
        self.__left = None
        self.__right = None
        
    def insert(self, key, info):
        '''creates a new node containing key in the BST.
If key already exists, the previous info value is replaced by the current info and returns False, otherwise a new node (with two dummy leaves) is added and returns True'''
        if self.__key is None: # tree was empty, just create the root
            self.__key = key
            self.__info = info
            self.__left = BST()    # dummy leaf (empty left subtree)
            self.__right = BST()   # dummy leaf (empty right subtree)
            return True
        elif key < self.__key:    # root is not dummy, with two children (each one is possibly dummy)
            if self.__left.insert(key, info):
                return True
            else:
                return False
        elif key > self.__key:
            if self.__right.insert(key, info):
                return True
            else:
                return False
        else: # key == self.__key
            self.__info = info  # just replace the info associated to the existing key
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
        if self.__key is None or self.__left.__key is None:
            return self.__key, self.__info
        else:
            return self.__left.minimum()
        
    def maximum(self):
        '''returns the pair key, info for the maximum key in the BST.
Returns None if the tree is empty'''
        if self.__key is None or self.__right.__key is None:
            return self.__key, self.__info
        else:
            return self.__right.maximum()
        
    def delete(self, key):
        '''deletes an item in the BST, if it exists'''
        if self.search(key) is None: # key does not exist
            return self
            
        if key == self.__key and self.__left.__key is None: # key is the only node in the BST
            self.__key = None                               # BST is empty after deletion
            self.__info = None
            self.__left = None
            self.__right = None
            return self   # result is the modified tree
        if key < self.__key:
            self.__left = self.__left.delete(key)  # returns the new subtree
            return self
        elif key > self.__key:
            self.__right = self.__right.delete(key)
            return self
        else: # key == self.__key
            if self.__left.__key is None:  # no left child (empty left subtree)
                return self.__right
            elif self.__right.__key is None:  # no right child
                return self.__left
            else:                          # both children exist, replace root by the minimum in right subtree
                self.__key, self.__info = self.__right.minimum() # replace with successor
                self.__right = self.__right.delete(self.__key)   # delete successor
                return self
    
    def height(self):
        if self.__key is None:
            return 0
        else:
            return 1 + max(self.__left.height(), self.__right.height())

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
    print(f' height = {a.height()}')


a = BST()

items = [[23, 230], [12, 120], [44, 440], [11, 110], [10, 100], [13, 130], [40, 400], [45, 450], [42, 420]]
for x in items:
    a.insert(*x)

a.print_tree()
print("pre-order:", a.pre_order_visit())
print("in-order:", a.in_order_visit())
print("post-order:", a.post_order_visit())

l = a.in_order_visit()   # list of elements in increasing order [(k, v), (k, v), ...., (k, v)]

print(f'minimum: {a.minimum()}')
print(f'maximum: {a.maximum()}')

print("height:", a.height())
delete_and_print(22)
delete_and_print(30)
delete_and_print(45)
delete_and_print(44)
delete_and_print(23)
delete_and_print(12)    
delete_and_print(10)
delete_and_print(11)
delete_and_print(40)
delete_and_print(13)
delete_and_print(42)
print(a.search(42))
delete_and_print(42)

