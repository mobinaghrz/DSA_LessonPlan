class Node:
    def __init__(self, data, nextNode=None):
        """
        Input:
            - data: the value to be stored in the node
            - nextNode: a reference to the next node in the list
                        (defaults to None)

        Output:
            - void (initializes a new Node object)

        Description:
            The Node class represents a single element in a linked list.

            Each Node contains:
                - 'data': the stored value
                - 'next': a pointer/reference to the next node in the list

            When a new Node is created, its 'data' field is set to the given
            value, and its 'next' field is set to either:
                - the provided nextNode, or
                - None, if no next node is supplied.

            This structure allows nodes to be chained together to form
            a linked list.

        Time Complexity:
            - O(1), simple assignment operations

        Space Complexity:
            - O(1), one node object with constant fields
        """
        self.data = data
        self.next = nextNode


class LinkedList:
    def __init__(self, node=None):
        """
        Input:
            - node: an initial Node object to serve as the head and tail
                    of the linked list (defaults to None)

        Output:
            - void (initializes an empty or single-node linked list)

        Description:
            The LinkedList class manages a sequence of Node objects.

            Initialization Behavior:
                - If 'node' is None:
                    - The list is initialized as empty
                    - head = None
                    - tail = None
                    - size = 0
                - If a Node is provided:
                    - The list begins with that single node
                    - head = node
                    - tail = node
                    - size = 1

            This setup ensures that the linked list always tracks:
                - its first node (head)
                - its last node (tail)
                - its current size

            These attributes allow efficient insertion and traversal operations.

        Time Complexity:
            - O(1), constant-time initialization

        Space Complexity:
            - O(1), stores a fixed number of attributes
        """
        self.head = node
        self.tail = node
        self.size = 0 if self.head is None else 1
