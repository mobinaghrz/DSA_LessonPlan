class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next



class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.size = 0 if self.head is None else 1

    def add_first(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1
        
    def add_last(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def insert(self, value, index):
        """
        Input:
            - value: the data to be stored in the new node
            - index: the position at which the new node should be inserted
                    (0 ≤ index ≤ size of the list)

        Output:
            - void (updates the linked list by inserting a new node at 
                    the specified index)

        Description:
            The insert method adds a new node containing the given value
            at the specified index within the doubly linked list.

            Process:
                - If the index is invalid (less than 0 or greater than size),
                an exception is raised.
                - If index is 0:
                    - Call add_first to insert at the head.
                - If index equals the current size:
                    - Call add_last to insert at the tail.
                - Otherwise (insertion in the middle):
                    - Create a new Node with the provided value.
                    - Traverse the list to find the node just before the target index.
                    - Set new_node.next to the node currently at the insertion index.
                    - Set new_node.prev to the node at index - 1.
                    - Update the surrounding nodes’ pointers:
                        - The previous node’s next should point to new_node.
                        - The next node’s prev should point to new_node.
                - Increase the size of the list by 1.

            This method ensures proper maintenance of both next and prev
            references, preserving the structure of the doubly linked list.

        Time Complexity:
            - O(n) due to traversal to reach the insertion point
            (can be optimized by backward traversal for large indexes)

        Space Complexity:
            - O(1), only one new node and a constant amount of additional references
            are created
        """
        if index < 0 or index > self.size:
            raise Exception("index out of range")
        
        if index == 0:
            self.add_first(value)
            return
        
        if index == self.size:
            self.add_last(value)
            return
        
        new_node = Node(value)
        
        #TODO: Implement backward iterating to decrease the comparisons
        itr = self.head
        for _ in range(index - 1):
            itr = itr.next
            
        new_node.next = itr.next
        new_node.prev = itr
        
        itr.next.prev = new_node
        itr.next = new_node
        
        self.size += 1
