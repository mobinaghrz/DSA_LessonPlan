class Node:
    def __init__(self, data, nextNode=None):
        self.data = data
        self.next = nextNode
        

class LinkedList:
    def __init__(self, node=None):
        self.head = node 
        self.tail = node 
        self.size = 0 if self.head is None else 1
        
    def traverse(self):
        itr = self.head
        while itr is not None:
            print(itr.data)
            itr = itr.next
            
    def search(self, aim):
        itr = self.head
        while itr is not None:
            if itr.data == aim:
                print("Found it!")
                break
            itr = itr.next
            
    def add_first(self, value):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

        self.size += 1 
        
    def add_last(self, value):
        newNode = Node(value)

        if self.tail is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

        self.size += 1
        
    def insert(self, value, index):
        """
        Input:
            - value: the data to be inserted into the linked list
            - index: the position at which the new value should be inserted
                    (0 ≤ index ≤ size)

        Output:
            - void (updates the linked list by inserting a new node at
                    the specified index)

        Description:
            The insert method places a new node containing the given value
            at a specific index in the linked list.

            Valid index range:
                - 0 (insert at the beginning)
                - size (insert at the end)
                - Any index in between

            Special Cases:
                - If index == 0:
                    - Call add_first(value) to insert at the head.
                - If index == size:
                    - Call add_last(value) to insert at the tail.

            General Case (insertion in the middle):
                - Start from the head and move forward until reaching
                the node immediately before the target index.
                - Create a new node.
                - Set newNode.next to the successor node.
                - Set the previous node’s next pointer to the new node.
                - Increase size by 1.

            This method ensures that all link adjustments maintain list integrity.

        Time Complexity:
            - O(n), because reaching the insertion point requires traversal
            - Best case: O(1) when inserting at head or tail

        Space Complexity:
            - O(1), only a single new node and constant pointers are used
        """
        if index < 0 or index > self.size:
            raise Exception("index out of range")

        if index == 0:
            self.add_first(value)
            return

        if index == self.size:
            self.add_last(value)
            return

        counter = 0
        prevNode = self.head
        while counter + 1 != index:
            prevNode = prevNode.next
            counter += 1

        newNode = Node(value)
        newNode.next = prevNode.next
        prevNode.next = newNode
        self.size += 1
