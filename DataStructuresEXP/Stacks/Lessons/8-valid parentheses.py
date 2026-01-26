class Node:
    def __init__(self, value):
        self.value = value
        self.rear = None


class Stack:
    def __init__(self):
        self.size = 0
        self.top = None

    def push(self, data):
        new_node = Node(data)

        new_node.rear = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if (self.top is None):
            print("Stack is empty")
            return 
        
        data = self.top
        self.top = self.top.rear
        self.size -= 1

        return data.value
    
    def peek(self):
        if self.top is None:
            print("Stack is empty")
            return
        
        return self.top.value
    

def is_valid(parentheses):
    my_stack = Stack()

    for par in parentheses:
        if par == "(":
            my_stack.push(par)
        else:
            if my_stack.size == 0:
                return False 
            
            my_stack.pop()

    return my_stack.size == 0

print(is_valid("(()(()))"))
print(is_valid("(()(()"))
