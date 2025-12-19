class Node:
    """
    Input:
        - value:
            - The data element to be stored in the node.
            - Can be of any type.

    Output:
        - None.

    Description:
        The constructor initializes a single node used in a
        linked-list–based stack implementation.

        Each node contains:
            - `value`: the data stored in the stack
            - `rear`: a reference to the next node in the stack

        In this stack design:
            - The `rear` attribute points to the node directly
                below the current node in the stack.
            - The node at the top of the stack has its `rear`
                pointing to the next element in LIFO order.
            - The bottom node of the stack has `rear == None`.

        This node structure enables constant-time push and pop
        operations by updating only the stack's `top` reference.

        Process:
            - Step 1: Assign the provided value to the node:
                self.value = value

            - Step 2: Initialize the link to the next node:
                self.rear = None

    Invariants established:
        - self.value always stores the data associated with the node.
        - self.rear is either:
            - None (for the bottom node), or
            - A reference to another Node instance.
        - Nodes form a singly linked chain.

    Time Complexity:
        - O(1), as initialization involves constant-time assignments.

    Space Complexity:
        - O(1), one node is created per element stored.
    """
    def __init__(self, value):
        self.value = value
        self.rear = None


class Stack:
    """
    Input:
        - None.

    Output:
        - None.

    Description:
        The constructor initializes an empty stack implemented
        using a linked list.

        The stack maintains:
            - `top`: a reference to the node at the top of the stack
            - `size`: the number of elements currently in the stack

        At initialization:
            - The stack contains no elements.
            - `top` is set to None to indicate the stack is empty.
            - `size` is set to 0.

        This method establishes the base invariants required
        for all stack operations such as push, pop, and peek.

        Invariants established:
            - self.size == 0
            - self.top == None
            - If self.size == 0, the stack is empty.
            - The stack follows LIFO (Last-In, First-Out) order
                once elements are added.

    Time Complexity:
        - O(1), as only constant-time assignments are performed.

    Space Complexity:
        - O(1), no additional memory is allocated beyond
            the stack object itself.
    """
    def __init__(self):
        self.size = 0
        self.top = None