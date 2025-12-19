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
        """
        Input:
            - None (operates directly on the stack's internal state).

        Output:
            - The element removed from the top of the stack.
            - If the stack is empty:
                - Prints "Stack is empty"
                - Returns None.

        Description:
            The pop method removes and returns the top element of the stack.
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
                    - Retrieve the value stored at:
                        self.array[self.size - 1]
                    - Store it in a temporary variable `data`.

                - Step 3: Remove the element from the stack:
                    - Set the array slot to None to clear the reference:
                        self.array[self.size - 1] = None

                - Step 4: Update the stack size:
                    - Decrement self.size by 1 to reflect the removal.

                - Step 5: Return the removed value:
                    - Return:
                        data

            Invariants relied upon:
                - self.size always represents the number of valid elements.
                - Valid elements occupy indices:
                    0 to self.size - 1.
                - self.size is never negative.
                - The stack follows LIFO (Last-In, First-Out) order.

        Time Complexity:
            - O(1), because both access and removal occur at a known index.

        Space Complexity:
            - O(1), as no additional memory is allocated.
        """
        if (self.size == 0):
            print("Stack is empty")
            return

        data = self.array[self.size - 1]
        self.array[self.size - 1] = None

        self.size -= 1
        return data
    