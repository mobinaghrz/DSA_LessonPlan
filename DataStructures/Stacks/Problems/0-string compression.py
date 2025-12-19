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
    
    def is_empty(self):
        return self.size == 0    

size = int(input())
string = input()

def solution(size, string):
    st = Stack()

    for char in string:
        if not st.is_empty() and st.peek() == char:
            st.pop()
        else:
            st.push(char)

    temp = []

    while not st.is_empty():
        temp.append(st.pop())

    return "".join(temp)[::-1]

print(solution(size, string))