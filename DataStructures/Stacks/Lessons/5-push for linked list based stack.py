class Node:
    def __init__(self, value):
        self.value = value
        self.rear = None


class Stack:
    def __init__(self):
        self.size = 0
        self.top = None

    def push(self, data):
        """
        Input:
            - data:
                - The element to be added to the stack.
                - Can be of any type.

        Output:
            - None.

        Description:
            The push method inserts a new element at the top of the stack.

            The stack is implemented using a singly linked list.
            Each element is wrapped in a Node object, where:
                - `value` stores the data
                - `rear` references the next node in the stack

            The stack maintains:
                - `top`: a reference to the top node
                - `size`: the current number of elements

            This implementation handles both empty and non-empty
            stacks uniformly without requiring a conditional check.

            Process:
                - Step 1: Create a new node:
                    - Instantiate a Node with the provided data.

                - Step 2: Link the new node to the current stack:
                    - Assign the current top node to:
                        new_node.rear = self.top
                    - Update the stack's top reference:
                        self.top = new_node

                - Step 3: Update the stack size:
                    - Increment self.size by 1.

            Invariants relied upon:
                - self.top always references the top node of the stack.
                - If the stack was empty:
                    - self.top was None before insertion.
                    - new_node.rear is set to None.
                - If the stack was not empty:
                    - new_node.rear references the previous top node.
                - self.size accurately reflects the number of elements.
                - The stack follows LIFO (Last-In, First-Out) order.

        Time Complexity:
            - O(1), as insertion occurs at the top with constant-time
              pointer updates.

        Space Complexity:
            - O(1), one new node is allocated per push operation.
        """
        new_node = Node(data)

        new_node.rear = self.top
        self.top = new_node
        self.size += 1