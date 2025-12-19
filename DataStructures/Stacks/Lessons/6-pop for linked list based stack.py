class Node:
    def __init__(self, value):
        self.value = value
        self.rear = None


class Stack:
    def __init__(self):
        self.size = 0
        self.top = None

    def push(self, data):
        new_node = Node(data)

        new_node.rear = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        """
        Input:
            - None (operates directly on the stack's internal state).

        Output:
            - The value stored at the top of the stack.
            - If the stack is empty:
                - Prints "Stack is empty"
                - Returns None.

        Description:
            The pop method removes and returns the top element of the stack.

            The stack is implemented using a singly linked list.
            Each element is stored in a Node object, where:
                - `value` holds the data
                - `rear` references the next node in the stack

            The stack maintains:
                - `top`: a reference to the top node
                - `size`: the number of elements currently in the stack

            Process:
                - Step 1: Check for stack underflow:
                    - If self.top is None:
                        - The stack is empty.
                        - Print "Stack is empty".
                        - Exit the method without modifying the stack.

                - Step 2: Store the current top node:
                    - Assign the node referenced by self.top to a
                      temporary variable `data`.

                - Step 3: Remove the top node:
                    - Update self.top to reference:
                        self.top.rear

                - Step 4: Update the stack size:
                    - Decrement self.size by 1.

                - Step 5: Return the removed value:
                    - Return:
                        data.value

            Invariants relied upon:
                - If self.size == 0, self.top is None.
                - If self.size > 0, self.top references a valid Node.
                - self.size always reflects the number of elements.
                - Nodes are linked in LIFO (Last-In, First-Out) order.
                - self.size is never negative.

        Time Complexity:
            - O(1), as removal occurs at the top of the stack.

        Space Complexity:
            - O(1), no additional memory is allocated.
        """
        if (self.top is None):
            print("Stack is empty")
            return 
        
        data = self.top
        self.top = self.top.rear
        self.size -= 1

        return data.value