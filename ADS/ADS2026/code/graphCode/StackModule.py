from linkedListClass import LinkedList

class Stack:
    
    def __init__(self):
        self.__stack = LinkedList()
        
    def empty(self):
        return self.__stack.empty()
    
    def push(self, val):
        self.__stack.insert_front(val)
        
    def top(self):
        return(self.__stack.get_head())
        
    def remove(self):
        self.__stack.remove_head()
        
    def pop(self):
        '''remove the top element and return its value'''
        v = self.__stack.get_head()
        self.__stack.remove_head()
        return(v)
        

if __name__ == "__main__":
    s = Stack()
    s.push(100)  #  100
    s.push(200)   # 200, 100
    s.push(300)  #  300, 200, 100
    print(s.top())  #        -> 300
    print(s.top())  #        -> 300
    print(s.pop())  # 200, 100
    print(s.pop())  # 100
    s.push(12)      # 12, 100
    while not s.empty():
        print(s.pop())
