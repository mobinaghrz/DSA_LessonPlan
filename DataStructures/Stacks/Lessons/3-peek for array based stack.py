class Stack:
    def __init__(self, max_size):
        self.size = 0 
        self.max_size = max_size
        self.array = [None] * max_size

    def push(self, value):
        if (self.size == self.max_size):
            print("Stack is Full")
            return
        
        self.array[self.size] = value
        self.size += 1

    def pop(self):
        if (self.size == 0):
            print("Stack is empty")
            return

        data = self.array[self.size - 1]
        self.array[self.size - 1] = None

        self.size -= 1
        return data
    
    def peek(self):
        """
        Input:
            - None (operates directly on the stack's internal state).

        Output:
            - The element currently at the top of the stack.
            - If the stack is empty:
                - Prints "Stack is empty"
                - Returns None.

        Description:
            The peek method returns the top element of the stack
            without removing it.

            The stack is implemented using a fixed-size array, and the
            `size` attribute tracks the current number of elements.

            The top of the stack is always located at index:
                self.size - 1

            Process:
                - Step 1: Check for stack underflow:
                    - If self.size == 0:
                        - The stack is empty.
                        - Print "Stack is empty".
                        - Exit the method without modifying the stack.

                - Step 2: Access the top element:
                    - Retrieve and return the value stored at:
                        self.array[self.size - 1]

            Invariants relied upon:
                - self.size always represents the number of valid elements.
                - Valid elements occupy indices:
                    0 to self.size - 1.
                - self.size is never negative.
                - The stack follows LIFO (Last-In, First-Out) order.
                - The stack state is not modified by this method.

        Time Complexity:
            - O(1), because the top element is accessed directly.

        Space Complexity:
            - O(1), as no additional memory is allocated.
        """
        if (self.size == 0):
            print("Stack is empty")
            return
        
        return self.array[self.size - 1]