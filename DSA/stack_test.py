from collections import deque

stk = deque()
stk.append(5)
stk.append(89)
print(stk.pop())

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
    
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    



if __name__ == '__main__':
    s = Stack()
    s.push(10)
    print(s.peek())
    print(s.pop())
    print(s.is_empty())
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.size())
    
        