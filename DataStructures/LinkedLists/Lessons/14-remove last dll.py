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
        """
        Input:
            - None (operates directly on the linked list structure)

        Output:
            - void (removes the last node of the doubly linked list and 
                    updates the tail accordingly)

        Description:
            The remove_last method removes the node at the end (tail)
            of the doubly linked list.

            Process:
                - If the list is empty (head is None):
                    - Raise an exception because there is no node to remove.
                - If the list contains only one node (head is tail):
                    - Set both head and tail to None, leaving the list empty.
                - Otherwise:
                    - Temporarily store a reference to the current tail.
                    - Move tail to the previous node.
                    - Set the new tail's next pointer to None.
                    - Disconnect the removed node by clearing its prev pointer.
                - Decrease the size of the list by 1.

            This method correctly updates both next and prev references,
            maintaining a valid doubly linked list structure after the removal.

        Time Complexity:
            - O(1), removal from the tail requires no traversal

        Space Complexity:
            - O(1), no additional memory beyond a temporary reference
            is used
        """
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
