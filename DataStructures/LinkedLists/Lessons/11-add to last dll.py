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
        """
        Input:
            - value: the data to be stored in the new node added
                    at the end of the doubly linked list

        Output:
            - void (updates the linked list by inserting a new node at the tail)

        Description:
            The add_last method inserts a new node containing the given value
            at the end (tail) of the doubly linked list.

            Process:
                - Create a new Node with the provided value.
                - If the list is empty (head is None):
                    - Set both head and tail to the new node, since it becomes the only node.
                - Otherwise:
                    - Set new_node.prev to point to the current tail.
                    - Set the current tail.next to point to the new node.
                    - Update tail so that it becomes the new node.
                - Increase the size of the list by 1.

            This method ensures constant-time insertion at the end of the
            doubly linked list while maintaining correct forward and backward links.

        Time Complexity:
            - O(1), insertion at the tail requires no traversal

        Space Complexity:
            - O(1), only one additional node reference is created
        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1
