class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 
        self.prev = None


class Queue:
    def __init__(self):
        self.front = None 
        self.back = None
        self.middle = None
        self.size = 0

    def show_status(self):
        if self.is_empty():
            print(-1)
            return

        itr = self.front

        while itr is not self.back:
            print(f"{itr.data} ", end="")
            itr = itr.next

        print(itr.data)

    def is_empty(self):
        return self.front is None and self.middle is None and self.back is None
    
    def push_front(self, value):
        new_node = Node(value)
        
        if self.is_empty():
            self.front = new_node
            self.middle = new_node
            self.back = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
    
            if self.size % 2 == 1:
                self.middle = self.middle.prev

        self.size += 1

    def push_middle(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.front = new_node
            self.middle = new_node
            self.back = new_node
        elif self.size == 1:
            new_node.next = self.front
            self.front.prev = new_node

            self.front = self.front.prev
            self.middle = self.middle.prev
        elif self.size == 2:
            new_node.next = self.back
            new_node.prev = self.front

            self.middle = new_node

            self.front.next = self.middle
            self.back.prev = self.middle
        else:
            if self.size % 2 == 1:
                new_node.prev = self.middle.prev
                new_node.next = self.middle

                self.middle.prev.next = new_node
                self.middle.prev = new_node
            else:
                new_node.prev = self.middle
                new_node.next = self.middle.next

                self.middle.next.prev = new_node
                self.middle.next = new_node 
                
            self.middle = new_node

        self.size += 1

    def push_back(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.front = new_node
            self.middle = new_node
            self.back = new_node
        else:
            new_node.prev = self.back
            self.back.next = new_node
            self.back = new_node

            if self.size % 2 == 0:
                self.middle = self.middle.next

        self.size += 1

    def pop_front(self):
        if self.is_empty():
            return
        elif self.size == 1:
            self.front = None 
            self.middle = None 
            self.back = None
        elif self.size == 2:
            self.front.next = None 
            self.back.prev = None
            
            self.front = self.back
            self.middle = self.back
        else:
            temp = self.front
            self.front = temp.next

            temp.next = None 
            self.front.prev = None

            if self.size % 2 == 0:
                self.middle = self.middle.next 

        self.size -= 1

    def pop_middle(self):
        if self.is_empty():
            return
        elif self.size == 1:
            self.front = None 
            self.middle = None 
            self.back = None
        elif self.size == 2:
            self.front = self.back 

            self.middle.next = None 
            self.back.prev = None 

            self.middle = self.back
        else:
            temp = self.middle

            temp.prev.next = self.middle.next
            temp.next.prev = self.middle.prev

            if self.size % 2 == 0:
                self.middle = self.middle.next
            else:
                self.middle = self.middle.prev

            temp.next = None 
            temp.prev = None
        
        self.size -= 1

    def pop_back(self):
        if self.is_empty():
            return
        elif self.size == 1:
            self.front = None 
            self.middle = None 
            self.back = None
        else:
            temp = self.back 
            self.back = temp.prev

            self.back.next = None 
            temp.prev = None 

            if self.size % 2 == 1:
                self.middle = self.middle.prev 

        self.size -= 1

n = int(input())

def solution(ops):
    queue = Queue()

    for _ in range(ops):
        inputs = input().split(" ")

        if len(inputs) == 2:
            instruction, value = inputs[0], inputs[1]
        else:
            instruction = inputs[0]

        if instruction == "PushFront":
            queue.push_front(value) 
        elif instruction == "PushMiddle":
            queue.push_middle(value)
        elif instruction == "PushBack":
            queue.push_back(value)
        elif instruction == "PopFront":
            queue.pop_front()
        elif instruction == "PopMiddle":
            queue.pop_middle()
        elif instruction == "PopBack":
            queue.pop_back()

    queue.show_status()


solution(n)