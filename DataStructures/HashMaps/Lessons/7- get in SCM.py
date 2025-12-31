class Node:
    def __init__(self, key, value):
        self.data = (key, value)
        self.next = None
        

class LinkedList:
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
            self.head = newNode

        self.size += 1 
        
    def add_last(self, key, value):
        newNode = Node(key, value)

        if self.tail is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
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

        self.size -= 1

    def remove_last(self):
        if self.head is None:
            raise Exception("linked list is empty")
        elif self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            itr = self.head
            while itr.next is not self.tail:
                itr = itr.next

            itr.next = None
            self.tail = itr

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
            bucket = LinkedList()
            bucket.add_last(key, value)
            self.map[idx] = bucket
        else:
            node = bucket.search(key)

            if node is not None:
                node.data = (key, value)
            else:
                bucket.add_last(key, value)

    def search(self, key):
        """
        Input:
            - key: a string key identifying the entry to be searched for

        Output:
            - value or None:
                - Returns the value associated with the key if it exists
                - Returns None if the key does not exist in the hash map

        Description:
            This method searches for a key in the hash map and returns the value
            associated with that key.

            The search process works as follows:
                - Compute the bucket index using the hash function
                - Retrieve the bucket (linked list) at the computed index
                - If the bucket is empty (None), the key does not exist
                - Otherwise, traverse the linked list and compare stored keys
                - If a matching key is found, return its associated value
                - If the key is not found after traversal, return None

            This implementation handles hash collisions using separate chaining,
            meaning multiple keys that hash to the same index are stored in the
            same bucket list and searched sequentially.

        Time Complexity:
            - Average case: O(1) expected (assuming uniform hashing)
            - Worst case:  O(n) where n is the number of entries in a single bucket

        Space Complexity:
            - O(1), constant extra space is used
        """
        idx = self.hash(key)
        bucket = self.map[idx]
        
        if bucket is None:
            return
        
        node = bucket.search(key)
        
        if node is None:
            return 
        
        return node.data[1]