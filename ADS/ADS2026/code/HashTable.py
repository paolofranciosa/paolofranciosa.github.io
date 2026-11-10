import sympy
import hashlib

class HashElement:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.isdeleted = False
    
    def delete(self):
        self.isdeleted = True
        
    def deleted(self):
        return self.isdeleted
    
    def get_key(self):
        return self.key

    def get_val(self):
        return self.val

class HashTable:
    def __init__(self, n = 5):
        self.__n = n
        self.__count = 0
        self.__table = [None] * self.__n # creates a list containing n None elements
        self._step = 1
        
    def __hash_function(self, x):
        '''uses MD5 hash function'''
        hash_object = hashlib.md5(x.encode())
        md5_hash = hash_object.hexdigest()
        return int(md5_hash,16) # md5_hash is interpreted as a base 16 number

    def __search_position(self, k):
        address = self.__hash_function(k) % self.__n
#        print("retrieve {} from {}".format(k, address))
        while self.__table[address] is not None and (self.__table[address].deleted() or self.__table[address].get_key() != k):
            address = (address + self._step) % self.__n
#            print("  retrieve at", address)
        if self.__table[address] is None:
            return None
        else:
            return address 
    
    def retrieve(self, k):
        address = self.__search_position(k)
        if address is None:
            return None
        else:
            return self.__table[address].get_val()
        
    def delete(self, k):
        address = self.__search_position(k)
        if address is None:
            return None
        else:
            self.__count -= 1
            self.__table[address].delete()
        
    def insert(self, k, v, old_element = None):
        '''inserts an item in the HashTable. If old_element is None a new HashElement is created
containing k, v, otherwise element old_element is inserted'''
        # check here whether there is room for the new entry, count < 0.7 * n
        if self.__count >= 0.7 * self.__n:
            self.__double()
        if old_element is None:
            element = HashElement(k,v)
        else:
            element = old_element
        address = self.__hash_function(element.get_key()) % self.__n
#        print("insert {} from {}".format(element.get_key(), address))
        while (self.__table[address] is not None) and (not self.__table[address].deleted()):
            address = (address + self._step) % self.__n
#            print("  insert at", address)
        self.__count += 1
        self.__table[address] = element

    def __double(self):
        '''reallocates elements in a new table, doubling the size'''
        print("         start doubling")
        self.__n = sympy.nextprime(2 * self.__n)
        old_table = self.__table
        self.__table = [None] * self.__n
        self.__count = 0
        for el in old_table:
            if el is not None and not el.deleted():
                self.insert(None, None, el)
#        print("         done")
        
        
