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
        if index < 0 or index > self.size:
            raise Exception("index out of range")

        if index == 0:
            self.add_first(value)
            return

        if index == self.size:
            self.add_last(value)
            return

        counter = 0
        prev_node = self.head
        while counter + 1 != index:
            prev_node = prev_node.next
            counter += 1

        newNode = Node(value)
        newNode.next = prev_node.next
        prev_node.next = newNode
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
        
    def remove(self, index):
        """
        Input:
            - index: the position of the node to remove
                    (0 ≤ index < size)

        Output:
            - void (removes the node at the specified index)

        Description:
            The remove method deletes a node from a specific position
            in the linked list.

            Validation:
                - If index is outside the valid range (less than 0 or
                greater than or equal to size), an exception is raised.

            Special Cases:
                - If index == 0:
                    - Call remove_first() to delete the head node.

                - If index == size - 1:
                    - Call remove_last() to delete the tail node.

            General Case (removal from the middle):
                - Traverse the list starting at the head until reaching
                the node immediately before the target index.
                - Store a reference to the target node.
                - Redirect the predecessor's next pointer to the target's
                successor.
                - Disconnect the removed node by setting its next reference
                to None.
                - Decrease the size by 1.

            This method ensures safe removal at any valid index while
            preserving the structure of the linked list.

        Time Complexity:
            - O(n), due to traversal required to reach the node before
            the one being removed

        Space Complexity:
            - O(1), uses only a small number of temporary pointers
        """
        if index < 0 or index >= self.size:
            raise Exception("index out of range")

        if index == 0:
            self.remove_first()
            return

        if index == self.size - 1:
            self.remove_last()
            return

        counter = 0
        itr = self.head
        while counter + 1 != index:
            itr = itr.next
            counter += 1

        target_node = itr.next
        itr.next = target_node.next
        target_node.next = None
        self.size -= 1
