class Node:
    def __init__(self, data, position):
        self.data = data
        self.position = position
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.holder = []

    def add(self, value, position):
        new_node = Node(value, position)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.holder.append(new_node)

    def load(self, size):
        for i in range(size):
            self.add(1, i+1)

    def put_to_sleep(self, pos):
        idx = pos - 1
        target = self.holder[idx]

        if target is self.head:
            return
        
        if target is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
            return

        target.prev.next = target.next
        target.next.prev = target.prev

        target.data = 0
    
    def find_next_one(self, pos):
        idx = pos - 1
        target = self.holder[idx]

        if target is self.tail:
            return -1

        return target.next.position


n, q = map(int, input().split())

def solution(size, ops):
    sequence = LinkedList()
    sequence.load(size)

    for _ in range(ops):
        op, pos = map(int, input().split())

        if op == 2:
            sequence.put_to_sleep(pos)
        else:
            next_one_position = sequence.find_next_one(pos)
            print(next_one_position)

solution(n, q)