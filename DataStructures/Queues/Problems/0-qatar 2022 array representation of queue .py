class Queue:
    def __init__(self):
        self.array = []
        self.front = -1
        self.middle = -1
        self.back = -1 
        
    def is_empty(self):
        return len(self.array) == 0
    
    def get_last_index(self):
        return len(self.array) - 1
    
    def get_length(self):
        return len(self.array)

    def update_middle(self):
        if self.get_length() == 1:
            self.middle = 0
        elif self.get_length() % 2 == 1:
            self.middle = self.get_length() // 2
        else:
            self.middle = self.get_length() // 2 - 1  

    def show_status(self):
        if self.is_empty():
            print(-1)
            return
        
        for element in self.array:
            print(f"{element}", end=" ")

        # print()
        # print(f"front: {self.array[self.front]}")
        # print(f"middle: {self.array[self.middle]}")
        # print(f"back: {self.array[self.back]}")
        # print("-" * 10)
        
    def push_front(self, value):
        if self.is_empty():
            self.array.insert(0, value)
            self.front = 0
            self.middle = 0
            self.back = 0
        else:
            self.array.insert(0, value)

            self.back = self.get_last_index()

            self.update_middle()

    def push_middle(self, value):
        if self.is_empty():
            self.array.insert(0, value)
            self.front = 0
            self.middle = 0
            self.back = 0
        else:
            idx = self.get_length() // 2
            self.array.insert(idx, value)
            self.back = self.get_last_index()
            self.update_middle()

    def push_back(self, value):
        if self.is_empty():
            self.array.insert(0, value)
            self.front = 0
            self.middle = 0
            self.back = 0
        else:
            self.array.append(value)

            self.back = self.get_last_index()

            self.update_middle()

    def pop_front(self):
        if self.is_empty():
            return
        
        self.array.pop(self.front)
        
        if self.get_length() == 0:
            self.front = -1
            self.middle = -1
            self.back = -1
        else:
            self.back = self.get_last_index()

            self.update_middle()
            
    def pop_middle(self):
        if self.is_empty():
            return

        self.array.pop(self.middle)

        self.update_middle()
        self.back = self.get_last_index()

        if self.get_length() == 0:
            self.front = -1
            self.back = -1

    def pop_back(self):
        if self.is_empty():
            return

        self.array.pop(self.back)

        if self.get_length() == 0:
            self.front = -1
            self.middle = -1
            self.back = -1
        else:
            self.back = self.get_last_index()

            self.update_middle()

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