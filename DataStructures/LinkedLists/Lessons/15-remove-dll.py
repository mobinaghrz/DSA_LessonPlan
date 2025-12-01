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

    def remove_first(self):
        if self.head is None:
            raise Exception("doubly linked list is empty")
        
        if self.head is self.tail:
            self.head = None 
            self.tail = None
        else:
            temp = self.head
            self.head = temp.next 
            temp.next = None 
            self.head.prev = None
            
        self.size -= 1

    def remove_last(self):
        if self.head is None:
            raise Exception("doubly linked list is empty")
        
        if self.head is self.tail:
            self.head = None 
            self.tail = None
        else:
            temp = self.tail
            self.tail = temp.prev
            self.tail.next = None 
            temp.prev = None
            
        self.size -= 1

    def remove(self, index):
        """
        Input:
            - index: the position of the node to be removed
                    (0 ≤ index < size of the list)

        Output:
            - void (removes the node at the specified index from the
                    doubly linked list)

        Description:
            The remove method deletes the node located at the given index
            within the doubly linked list.

            Process:
                - If the index is invalid (less than 0 or greater than or equal 
                to the size of the list), raise an exception.
                - If index is 0:
                    - Call remove_first to delete the head node.
                - If index is the last position (size - 1):
                    - Call remove_last to delete the tail node.
                - Otherwise (removal from the middle):
                    - Traverse the list to reach the node just before the 
                    target index.
                    - Store a reference to the node being removed.
                    - Update the surrounding links:
                        - Set itr.next to the node after the one being removed.
                        - Set that node’s prev pointer back to itr.
                    - Disconnect the removed node by clearing its next and prev
                    pointers.
                - Decrease the size of the list by 1.

            This method ensures consistent maintenance of both next and prev
            pointers during a middle removal, preserving the integrity of the 
            doubly linked list.

        Time Complexity:
            - O(n), due to traversal required to reach the specified index

        Space Complexity:
            - O(1), no additional memory beyond a temporary reference is needed
        """
        if index < 0 or index >= self.size:
            raise Exception("index out of range")
        
        if index == 0:
            self.remove_first()
            return 
        
        if index == self.size - 1:
            self.remove_last()
            return
        
        itr = self.head 
        for _ in range(index - 1):
            itr = itr.next
            
        temp = itr.next
        itr.next = temp.next
        temp.next.prev = itr
        
        temp.next = None 
        temp.prev = None 
        
        self.size -= 1
