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
            itr = itr.next
            
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
    
    def insert(self, key, value):
        idx = self.hash(key)
        bucket = self.map[idx]

        if bucket is None:
            bucket = DoublyLinkedList()
            bucket.add_last(key, value)
            self.map[idx] = bucket
        else:
            node = bucket.search(key)

            if node is not None:
                node.data = (key, value)
            else:
                bucket.add_last(key, value)

    def get(self, key):
        idx = self.hash(key)
        bucket = self.map[idx]
        
        if bucket is None:
            return
        
        node = bucket.search(key)
        
        if node is None:
            return 
        
        return node.data[1]
    
    def delete(self, key):
        """
        Input:
            - key: a string key identifying the entry to be deleted

        Output:
            - None

        Description:
            This method removes the key-value pair associated with the provided key
            from the hash map.

            The deletion process works as follows:
                - Compute the bucket index using the hash function
                - Retrieve the bucket (linked list) stored at the computed index
                - If the bucket is empty (None) or contains no nodes, raise an exception
                indicating the key is not found
                - Traverse the linked list to locate the node whose stored key matches
                the provided key
                - If the matching node is the head of the list, remove it using remove_first()
                - If the matching node is the tail of the list, remove it using remove_last()
                - If the matching node is in the middle, unlink it by reconnecting its
                previous and next neighbors and decrement the bucket size
                - If the deletion causes the bucket to become empty, set the bucket slot
                in the underlying array to None to fully remove the bucket

            This implementation handles hash collisions via separate chaining, so deletion
            only affects the linked list stored at the computed bucket index.

        Time Complexity:
            - Average case: O(1) expected (assuming uniform hashing)
            - Worst case:  O(n) where n is the number of entries in a single bucket

        Space Complexity:
            - O(1), constant extra space is used per operation
        """

        idx = self.hash(key)
        bucket = self.map[idx]

        if bucket is None or bucket.head is None:
            raise Exception("key not found")

        itr = bucket.head

        if itr.data[0] == key:
            bucket.remove_first()
            if bucket.size == 0:
                self.map[idx] = None
            return

        while itr is not None and itr.data[0] != key:
            itr = itr.next

        if itr is None:
            raise Exception("key not found")

        if itr.next is None:
            bucket.remove_last()
            if bucket.size == 0:
                self.map[idx] = None
            return

        itr.prev.next = itr.next
        itr.next.prev = itr.prev
        itr.next = None
        itr.prev = None
        bucket.size -= 1

        if bucket.size == 0:
            self.map[idx] = None
