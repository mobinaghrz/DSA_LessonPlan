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
    
    def is_empty(self):
        return self.size == 0    
    

def is_openning(char):
    return char.strip() in ["(", "[", "{"]

def is_match(openning, closing):
    paired = openning.strip() + closing.strip()
    return paired in ["()", "[]", "{}"]

_ = int(input())
parentheses = input()

def solution(par):
    my_stack = Stack()

    for par in parentheses:
        if is_openning(par):
            my_stack.push(par)
        else:
            if my_stack.is_empty():
                print("not valid")
                return
            
            openning = my_stack.pop()

            if not is_match(openning, par):
                print("not valid")
                return
            
    if my_stack.is_empty():
        print("valid")
    else:
        print("not valid")


solution(parentheses)