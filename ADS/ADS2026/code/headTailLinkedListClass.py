class Node:
    '''implements a node of a linked list'''
    def __init__(self, val, link = None):
        '''builds a new node containing a value. Parameter link is optional, its
value is assumed to be a reference to a node'''
        self.__value = val  # private variable storing information
        self.next = link
    
    def get_value(self):
        '''returns the value stored onto a node'''
        return self.__value
    
    
class LinkedList:
    '''implements a linked list with fast append / get_head / remove_head primitives'''
    def __init__(self):
        '''builds an empty linked list'''
        self.__head = None  # points to the head element 
        self.__tail = None  # points to the tail element
        
    def empty(self):
        '''returns True if and only if the list is empty'''
        return self.__head is None
    
    def append(self, val):
        '''creates a new Node containing val and appends it to the end of the list'''
        new_node = Node(val)  # new_node has None in the next field
        if self.__head is None:
            self.__head = new_node
            self.__tail = new_node
        else:  #  self is not empty
            self.__tail.next = new_node
            self.__tail = new_node
            
    def get_head(self):
        '''returns the fist value in the list. It is assumed the list is not empty'''
        return self.__head.get_value()

    def remove_head(self):
        '''removes the first element in the list, if the list is not empty'''
        if self.__head is not None:
            self.__head = self.__head.next
            if self.__head is None:
                self.__tail = None

    def get_list(self):
        '''returns a Python list (array of references) containing all elements in the list.
If list is empty, an empty list [] is returned'''
        res = []
        n = self.__head
        while n is not None:
            res.append(n.get_value())   #  Python list append method
            n = n.next    #  scan the LinkedList
        return res

