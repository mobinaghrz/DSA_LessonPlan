class Stack:
    """
    Input:
        - max_size (int):
            - The maximum number of elements the stack can hold.

    Output:
        - None (initializes the stack's internal state).

    Description:
        The __init__ method initializes a stack data structure with a
        fixed maximum capacity. It sets up the internal variables
        required to manage stack operations such as push and pop.

        The stack is implemented using a Python list (array-based stack),
        where elements are stored sequentially.

        Process:
            - Step 1: Initialize the current stack size:
                - Set self.size to 0, indicating the stack is empty.

            - Step 2: Store the maximum allowed size:
                - Assign the provided max_size to self.max_size.

            - Step 3: Allocate storage for the stack:
                - Create a list of length max_size filled with None:
                    self.array = [None] * max_size
                - This pre-allocates memory for stack elements.

        Invariants established:
            - self.size always represents the number of elements
            currently in the stack.
            - 0 ≤ self.size ≤ self.max_size.
            - self.array has a fixed length equal to self.max_size.
            - Valid stack elements occupy indices:
                0 to self.size - 1.

    Time Complexity:
        - O(n), where n = max_size, due to list initialization.

    Space Complexity:
        - O(n), where n = max_size, for storing the stack elements.
    """
    def __init__(self, max_size):
        self.size = 0 
        self.max_size = max_size
        self.array = [None] * max_size
