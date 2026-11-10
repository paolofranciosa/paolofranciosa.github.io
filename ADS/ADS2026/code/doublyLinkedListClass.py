class Node:

    def __init__(self, val, prec_el = None, next_el = None):
        self.__value = val
        self.next = next_el
        self.prec = prec_el
    
    def get_value(self):
        return self.__value
    

class DoublyLinkedList:

    def __init__(self):
        self.__head = None
        self.__tail = None
        
    def empty(self):
        return self.__head is None
    
    def insert_head(self, val):
        if self.__head is None:
            new_node = Node(val, None, None)
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node = Node(val, None, self.__head)
            self.__head.prec = new_node
            self.__head = new_node
            
    def insert_tail(self, val):
        if self.__head is None:
            new_node = Node(val, None, None)
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node = Node(val, self.__tail, None)
            self.__tail.next = new_node
            self.__tail = new_node
            
    def concatenate(self, other_list): # beware of termination: e.g. if other_list = self
        if self.__head is None:
            self.__head = other_list.__head
            self.__tail = other_list.__tail
        else:
            if other_list.__head is not None:
                self.__tail.next = other_list.__head
                other_list.__head.prec = self.__tail
                self.__tail = other_list.__tail
            
    def get_head(self):
        return self.__head.get_value()

    def get_tail(self):
        return self.__tail.get_value()

    def remove_head(self):
        if self.__head is not None:
            self.__head = self.__head.next
            self.__head.prec = None
            if self.__head is None:
                self.__tail = None

    def remove_tail(self):
        if self.__tail is not None:
            self.__tail = self.__tail.prec
            self.__tail.next = None
            if self.__tail is None:
                self.__head = None

    def contains(self, val):
        n = self.__head
        while n is not None:
            if n.get_value() == val:
                return True
            n = n.next
        return False
        
    def remove_val(self, val):
        if self.__head is None:  # empty list
            return
        
        n = self.__head
  # find the node containing val
        while n is not None and n.get_value() != val:
            n = n.next
        if n is not None:
            if n == self.__head:
                self.__head = n.next
                self.__head.prec = None
            else:
                if n == self.__tail:
                    self.__tail = n.prec
                    self.__tail.next = None
                else:
                    n.next.prec = n.prec
                    n.prec.next = n.next

    def get_list(self):
        res = []
        n = self.__head
        while n is not None:
            res.append(n.get_value())
            n = n.next
        return res
        
    def get_reverse_list(self):
        res = []
        n = self.__tail
        while n is not None:
            res.append(n.get_value())
            n = n.prec
        return res
