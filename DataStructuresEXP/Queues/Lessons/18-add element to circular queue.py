class CircularQueue:
    def __init__(self, size):
        self.array = [-1] * size
        self.front = -1
        self.rear = -1
        
    def get_size(self):
        return len(self.array)
        
    def is_empty(self):
        return self.front == -1 and self.rear == -1
    
    def is_full(self):
        return (self.rear + 1) % self.get_size() == self.front
    
    def enqueue(self, data):
        """
        Input:
            - data:
                The element/value to be inserted at the rear of the
                circular queue.

        Output:
            - None
                (Modifies the internal state of the queue in-place. If the
                queue is full, prints a message and does not insert.)

        Description:
            The enqueue method inserts a new element into the circular queue
            at the rear position, if there is available space.

            Process:
                - Step 1: Check if the queue is full:
                    - Call self.is_full().
                    - If it returns True:
                        - Print "Queue is full".
                        - Return immediately without inserting `data`.

                - Step 2: Handle the case where the queue is currently empty:
                    - Call self.is_empty().
                    - If it returns True:
                        - Set self.front = 0
                          This establishes index 0 as the front of the queue
                          for the first inserted element.

                - Step 3: Advance the rear pointer (circularly):
                    - Update self.rear as:
                        self.rear = (self.rear + 1) % self.get_size()
                    - This moves `rear` one step forward, wrapping around to
                      the beginning of the array when it reaches the end.

                    - Example:
                        - If rear == -1 initially and size == N:
                            self.rear = (-1 + 1) % N = 0
                          So the first element is placed at index 0.

                        - If rear is at the last index (N - 1):
                            self.rear = (N - 1 + 1) % N = 0
                          This wraps around to the start of the array.

                - Step 4: Insert the new element:
                    - Store the value in the internal array:
                        self.array[self.rear] = data

            Invariants relied upon:
                - An empty queue has:
                    - self.front == -1 and self.rear == -1
                - When inserting the very first element:
                    - front is set to 0, rear becomes 0 after the update.
                - Fullness is detected by:
                    (self.rear + 1) % self.get_size() == self.front

            Note:
                - For this method to work correctly with is_empty() and
                  is_full(), the corresponding dequeue method must:
                    - Update `front` using circular movement.
                    - Reset both `front` and `rear` to -1 when the last
                      element is removed.

        Time Complexity:
            - O(1), since it performs a constant number of checks, arithmetic
              operations, and a single assignment.

        Space Complexity:
            - O(1), as it uses only existing attributes and does not allocate
              additional data structures.
        """
        if self.is_full():
            print("Queue is full")
            return
        
        if self.is_empty():
            self.front = 0
            
        self.rear = (self.rear + 1) % self.get_size()
        self.array[self.rear] = data