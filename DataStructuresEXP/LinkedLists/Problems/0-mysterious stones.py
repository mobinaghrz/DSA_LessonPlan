_ = int(input())
stones = list(map(int, input().split()))

class Node:
    def __init__(self, value):
        self.data = value 
        self.prev = None 
        self.next = None 
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def add(self, value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
        self.size += 1
        
    def load(self, data):
        for d in data:
            self.add(d)
            
# Time Complexity O(n) 
def solution(stones):
    my_dll = DoublyLinkedList()
    
    my_dll.load(stones)
    
    if my_dll.size % 2 == 1:
        steps = my_dll.size // 2
    else:
        steps = my_dll.size // 2 - 1
        
    itr = my_dll.head
    for _ in range(steps):
        itr = itr.next
        
    while my_dll.size > 2:
        itr.prev.next = itr.next 
        itr.next.prev = itr.prev
        
        if my_dll.size % 2 == 1:
            temp = itr
            itr = itr.prev
        else:
            temp = itr
            itr = itr.next
            
        print(temp.data, end=" ")
        temp.next = None 
        temp.prev = None
        
        my_dll.size -= 1
        
    print(itr.data, itr.next.data , end=" ")
    
solution(stones)


# Time Compexity: O(n^2) (failed of course)
def firstattempt(stones):
    while len(stones) != 0:
        if len(stones) % 2 == 1:
            target_index = len(stones) // 2
        else:
            target_index = len(stones) // 2 - 1
        print(stones[target_index], end=" ")
        stones = stones[0:target_index] + stones[target_index+1:]