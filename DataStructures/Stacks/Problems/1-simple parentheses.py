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

    
n = int(input())
par = input()

def solution(size, parentheses):
    my_stack = Stack()
    indicies_container = []
    for i in range(size):
        if parentheses[i] == "(":
            my_stack.push(i+1)
        else:
            if my_stack.size == 0:
                print("not valid")
                return
            
            openning_i = my_stack.pop()
            indicies_container.append((openning_i, i+1))

    if my_stack.size != 0:
        print("not valid")
    else:
        print("valid")

        indicies_container.sort(key=lambda x: x[0])

        for t in indicies_container:
            print(f"{t[0]} {t[1]}")

solution(n, par)