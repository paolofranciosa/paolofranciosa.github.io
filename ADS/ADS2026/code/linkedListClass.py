class Node:
    '''implements a node of a linked list'''
    def __init__(self, val, link = None):
        '''builds a new node containing a value. Link parameter is optional, its
value is assumed to be a reference to a node, that is set as successor of the created node'''
        self.value = val  # variable storing information
        self.next = link
    
class LinkedList:
    '''Implements a linked list. Access is sequential, starting from the head element'''
    def __init__(self):
        '''builds an empty linked list'''
        self.__head = None
            
    def empty(self):
        '''returns True if and only if the list is empty'''
        return self.__head is None
    
    def insert_front(self, val):
        '''creates a new Node and inserts it in front of the list'''
        new_node = Node(val, self.__head)
        self.__head = new_node

    def append(self, val):
        '''creates a new Node and appends it to the end of the list'''
        if self.__head is None:
            self.insert_front(val)
        else:  #  self is not empty
            h = self.__head
            while h.next is not None:  # stop scanning before reaching the end
                h = h.next
            # h points now to the last Node
            new_node = Node(val)  # new_node has None in the next field
            h.next = new_node
            
    def concatenate(self, other_list):
        '''concatenates other_list to the end of the list. Elements in other_list are not copied.
Concatenating a list to itself produces a circular list'''
        if self.__head is None:
            self.__head = other_list.__head
        else:
            n = self.__head
            while n.next is not None:
                n = n.next
            n.next = other_list.__head
            
    def get_head(self):
        '''returns the first element in the list, if the list is not empty.
Returns None if the list is empty'''
        if self.__head is not None:
            return self.__head.value
        else:
            return None

    def remove_head(self):
        '''removes the first element in the list, if the list is not empty'''
        if self.__head is not None:
            self.__head = self.__head.next

    def contains(self, val):
        '''returns True if and only if the list contains at least one element equal (==) to val'''
        n = self.__head
        while n is not None:
            if n.value == val:
                return True
            n = n.next
        return False
        
    def remove_val(self, val):
        '''removes from the list the first element equal (==) to val'''
        if self.__head is None:  # empty list
            return
        
        if self.__head.value == val:   # remove the head node
            self.__head = self.__head.next
            return
        
        pred = self.__head
        n = pred.next
  # find the node containing val
  # maintaining a pointer to
  # its predecessor
        while n is not None and n.value != val:
            pred = n
            n = n.next
        if n is not None:
            pred.next = n.next
        
    def get_list(self):
        '''returns a Python list (array of references) containing all elements in the list.
If list is empty, an empty list [] is returned'''
        res = []
        n = self.__head
        while n is not None:
            res.append(n.value)   #  Python list append method
            n = n.next    #  scan the LinkedList
        return res
        
    def get_len(self):
        '''returns the number of nodes in the list'''
        return self.length(self.__head)
        
    def length(self, p):
        if p is None:
            return 0
        else:
            return 1 + self.length(p.next)
