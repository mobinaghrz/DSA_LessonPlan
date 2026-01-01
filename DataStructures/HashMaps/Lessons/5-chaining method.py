class Node:
    def __init__(self, key, value):
        self.data = (key, value)
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node 
        self.tail = node 
        self.size = 0 if self.head is None else 1
          
    def search(self, key):
        itr = self.head
        while itr is not None:
            if itr.data[0] == key:
                return itr
            
            
    def add_first(self, key, value):
        newNode = Node(key, value)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

        self.size += 1 
        
    def add_last(self, key, value):
        newNode = Node(key, value)

        if self.tail is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

        self.size += 1
        
    def remove_first(self):
        if self.head is None:
            raise Exception("linked list is empty")
        elif self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            target = self.head
            self.head = self.head.next

            target.next = None
            self.head.prev = None

        self.size -= 1

    def remove_last(self):
        if self.head is None:
            raise Exception("linked list is empty")
        elif self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            target = self.tail
            self.tail = target.prev

            target.prev = None
            self.tail.next = None
        self.size -= 1
        
class HashMap:
    def __init__(self, size):
        self.size = size 
        self.map = [None] * size

    def hash(self, key):
        hash_code = 0
        for char in key:
            hash_code += ord(char)
            
        index = hash_code % self.size 
        return index