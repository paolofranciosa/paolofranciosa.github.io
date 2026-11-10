class Number_set:
    '''This class manages a set of numeric elements.
The following operations are supported:
- inserting an element
- giving the number of elements in the set,
- giving the sum of elements in the set,
- giving the average value of elements in the set,
- ask whether the set is empty,
- reset the set to empty
- get the maximum inserted value
'''
    
    def __init__(self):  # constructor, builds an object (empty set)
        '''creates an object representing an empty set'''
        # define the "internal state" of the object. Variables inside each object
        self.__num = 0      # private variable
        self.__sum = 0      # private variable    INFORMATION HIDING
        self.__max = None   # private variable
        
    def add(self, val):  # modifier  adds a new element to the set
        '''adds item val to the set of numbers'''
        # update the internal status
        self.__num += 1
        self.__sum += val
        if self.__num == 1 or val > self.__max:
            self.__max = val        
        
    def reset(self):     # modifier, restores the initial condition (empty set)
        '''resets object to the empty set'''
        self.__num = 0
        self.__sum = 0
        self.__max = None
        
    def get_num(self):   # accessor, returns how many numbers have been added
        '''returns the number of inserted items'''
        return self.__num
    
    def get_sum(self):   # accessor, retuns the sum of elements
        '''returns the sum of inserted items'''
        return self.__sum
    
    def empty(self):   # accessor, retuns True if no elements have been added
        '''returns True if it is an empty set, False otherwise'''
        if self.__num == 0:
            return True
        else:
            return False
    
    def get_avg(self):   # accessor, returns the average of added elements
        '''returns the average of inserted items'''
        if self.__num == 0:
            return None
        else:
            return self.__sum/self.__num
    
    def get_max(self):   # accessor, returns the maximum
        '''returns the maximum item inserted to the set. Returns None if the set is empty'''
        return self.__max
