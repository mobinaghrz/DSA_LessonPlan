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
        """
        Input:
            - value: the data to be stored in the new node that will be added
                    at the beginning of the doubly linked list

        Output:
            - void (updates the linked list by inserting a new node at the head)

        Description:
            The add_first method inserts a new node containing the given value
            at the beginning (head) of the doubly linked list.

            Process:
                - Create a new Node with the provided value.
                - If the list is empty (head is None):
                    - Set both head and tail to the new node, as it is the only node.
                - Otherwise:
                    - Set new_node.next to the current head.
                    - Set the current head.prev to the new node.
                    - Update head so that it becomes the new node.
                - Increase the size of the list by 1.

            This method maintains proper forward (next) and backward (prev)
            references to ensure a valid doubly linked list structure.

        Time Complexity:
            - O(1), because insertion at the head of a linked list does not require traversal

        Space Complexity:
            - O(1), since only one new node and constant extra references are used
        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1
