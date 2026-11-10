from headTailLinkedListClass import LinkedList

class Queue:
    
    def __init__(self):
        self.__queue = LinkedList()
        
    def empty(self):
        return self.__queue.empty()
    
    def push(self, val):
        self.__queue.append(val)
        
    def top(self):
        return(self.__queue.get_head())
        
    def remove(self):
        self.__queue.remove_head()
        
    def pop(self):
        '''remove the top element e return its value'''
        v = self.__queue.get_head()
        self.__queue.remove_head()
        return(v)
        

if __name__ == "__main__":
    s = Queue()
    s.push(100)
    s.push(200) 
    print(s.pop())
    s.push(300) 
    print(s.pop()) 
    print(s.pop())
    s.push(400)
    s.push(500)    
    print(s.pop())
    s.push(600)
    print(s.pop())
    print(s.pop())

