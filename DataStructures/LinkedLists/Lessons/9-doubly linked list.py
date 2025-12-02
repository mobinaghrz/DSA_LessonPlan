class Node:
    def __init__(self, data, prev=None, next=None):
        """
        Input:
            - data: the value to be stored in this node
            - prev: a reference to the previous node in the list
                    (defaults to None)
            - next: a reference to the next node in the list
                    (defaults to None)

        Output:
            - void (initializes a new Node object)

        Description:
            The Node class represents a single element inside a
            doubly linked list.

            Each Node contains:
                - 'data': the stored value
                - 'prev': a pointer/reference to the previous node
                - 'next': a pointer/reference to the next node

            When a new Node is created:
                - 'data' is set to the given value
                - 'prev' is assigned the provided previous node or None
                - 'next' is assigned the provided next node or None

            This bidirectional linking allows traversal in both forward
            and backward directions, which is one of the key features of
            a doubly linked list.

        Time Complexity:
            - O(1), all operations are simple assignments

        Space Complexity:
            - O(1), each node stores a fixed amount of information
        """
        self.data = data
        self.prev = prev
        self.next = next



class DoublyLinkedList:
    def __init__(self, node=None):
        """
        Input:
            - node: an optional initial Node object that will serve as both
                    the head and tail of the list (defaults to None)

        Output:
            - void (initializes a new doubly linked list)

        Description:
            The DoublyLinkedList class manages a chain of Node objects that
            are linked in both directions.

            Initialization Behavior:
                - If 'node' is None:
                    - The list starts empty
                    - head = None
                    - tail = None
                    - size = 0
                - If a Node is provided:
                    - The list begins with that node
                    - head = node
                    - tail = node
                    - size = 1

            The class maintains:
                - 'head': the first node in the list
                - 'tail': the last node in the list
                - 'size': the number of nodes currently in the list

            Tracking both head and tail allows efficient insertions at
            either end, and the doubly linked structure enables
            movement forward and backward through the list.

        Time Complexity:
            - O(1), constant-time initialization

        Space Complexity:
            - O(1), only a few fixed attributes are stored
        """
        self.head = node
        self.tail = node
        self.size = 0 if self.head is None else 1
