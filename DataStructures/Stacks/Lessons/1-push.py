class Stack:
    def __init__(self, max_size):
        self.size = 0 
        self.max_size = max_size
        self.array = [None] * max_size

    def push(self, value):
        """
        Input:
            - value:
                - The element to be pushed onto the stack.

        Output:
            - None.
            - If the stack is full:
                - Prints "Stack is Full"
                - The value is not added.

        Description:
            The push method inserts a new element onto the top of the stack.
            The stack is implemented using a fixed-size array, and the
            `size` attribute tracks the current number of elements.

            The top of the stack is represented by the index `self.size`.

            Process:
                - Step 1: Check for stack overflow:
                    - If self.size == len(self.array):
                        - The stack has reached its maximum capacity.
                        - Print "Stack is Full".
                        - Exit the method without modifying the stack.

                - Step 2: Insert the new element:
                    - Store the value at index self.size:
                        self.array[self.size] = value

                - Step 3: Update the stack size:
                    - Increment self.size by 1 to reflect the new element.

            Invariants relied upon:
                - self.size always indicates the number of elements in the stack.
                - Valid stack elements are stored in indices:
                    0 to self.size - 1.
                - self.size never exceeds self.max_size.

        Time Complexity:
            - O(1), because insertion occurs at a known index.

        Space Complexity:
            - O(1), as no additional memory is allocated.
        """
        if (self.size == self.max_size):
            print("Stack is Full")
            return
        
        self.array[self.size] = value
        self.size += 1