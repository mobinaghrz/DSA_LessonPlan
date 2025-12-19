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
        if (self.top is None):
            print("Stack is empty")
            return 
        
        data = self.top
        self.top = self.top.rear
        self.size -= 1

        return data.value
    
    def peek(self):
        """
        Input:
            - None (operates directly on the stack's internal state).

        Output:
            - The value stored at the top of the stack.
            - If the stack is empty:
                - Prints "Stack is empty"
                - Returns None.

        Description:
            The peek method returns the value at the top of the stack
            without removing it.

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

                - Step 2: Access the top element:
                    - Return the value stored in:
                        self.top.value

            Invariants relied upon:
                - If self.size == 0, self.top is None.
                - If self.size > 0, self.top references a valid Node.
                - The stack state is not modified by this method.
                - The stack follows LIFO (Last-In, First-Out) order.

        Time Complexity:
            - O(1), as the top element is accessed directly.

        Space Complexity:
            - O(1), no additional memory is allocated.
        """
        if self.top is None:
            print("Stack is empty")
            return
        
        return self.top.value