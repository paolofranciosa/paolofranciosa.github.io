class Number_set:
    '''This class manages a set of numeric elements.
The following operations are supported:
- inserting an element
- giving the number of elements in the set,
- giving the sum of elements in the set,
- giving the average value of elements in the set,
- ask whether the set is empty,
- reset the set to empty,
- get the maximum inserted value

NEW FEATURES
- get the minimum inserted value,
- get the number of negative elements in the set,
- get the number of positive elements in the set,
- giving the variance of elements in the set
'''
    
    def __init__(self):  # constructor, builds an object (empty set)
        '''creates an object representing an empty set'''
        # define the "internal state" of the object. Variables inside each object
        self.num = 0      # member variable
        self.sum = 0               # member variable
        self.max = None            # member variable
    # ADDED VARIABLES FOR NEW REQUIREMENTS
        self.min = None            # member variable
        self.num_positive = 0      # member variable
        self.num_negative = 0      # member variable
        self.squares_sum = 0
        
    def add(self, val):  # modifier  adds a new element to the set
        '''adds item val to the set of numbers'''
        # update the internal status
        self.num += 1
        self.sum += val
        self.squares_sum += val * val
        if self.num == 1 or val > self.max:
            self.max = val        
        if self.num == 1 or val < self.min:
            self.min = val
        if val > 0:
            self.num_positive += 1
        if val < 0:
            self.num_negative += 1
        print(f"somma quadrati {self.squares_sum}")
        
    def reset(self):     # modifier, restores the initial condition (empty set)
        '''resets object to the empty set'''
        self.num = 0
        self.num_positive = 0
        self.num_negative = 0
        self.sum = 0
        self.squares_sum = 0
        self.max = None
        
    def get_num(self):   # accessor, returns how many numbers have been added
        '''returns the number of inserted items'''
        return self.num
    
    def get_num_negative(self):   # accessor, returns how many numbers have been added
        '''returns the number of inserted negative items'''
        return self.num_negative
    
    def get_num_positive(self):   # accessor, returns how many numbers have been added
        '''returns the number of inserted positive items'''
        return self.num_positive
    
    def get_sum(self):   # accessor, retuns the sum of elements
        '''returns the sum of inserted items'''
        return self.sum
    
    def empty(self):
        '''returns True if it is an empty set, False otherwise'''
        if self.num == 0:
            return True
        else:
            return False
    
    def get_avg(self):   # accessor, returns the average of added elements
        '''returns the average of inserted items'''
        if self.num == 0:
            return None
        else:
            return self.sum/self.num
    
    def get_variance(self):
        '''returns the variance of inserted items'''
        if self.num == 0:
            return None
        else:
            return self.squares_sum/self.num - self.get_avg()**2
    
    def get_max(self):
        '''returns the maximum item inserted to the set. Returns None if the set is empty'''
        return self.max
    
    def get_min(self):
        '''returns the minimum item inserted to the set. Returns None if the set is empty'''
        return self.min
