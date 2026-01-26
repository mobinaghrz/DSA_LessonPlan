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
        if self.is_full():
            print("Queue is full")
            return
        
        if self.is_empty():
            self.front = 0
            
        self.rear = (self.rear + 1) % self.get_size()
        self.array[self.rear] = data
        
    def dequeue(self):
        """
        Input:
            - None (operates directly on the queue's internal state).

        Output:
            - The element removed from the front of the circular queue.
            - If the queue is empty:
                - Prints "Queue is empty".
                - Returns None.

        Description:
            The dequeue method removes and returns the element at the
            front of the circular queue (FIFO behavior).

            Process:
                - Step 1: Check if the queue is empty:
                    - Call self.is_empty().
                    - If it returns True:
                        - Print "Queue is empty".
                        - Return None; no further processing is done.

                - Step 2: Read and clear the front element:
                    - Store the value:
                        data = self.array[self.front]
                    - Optionally clear that slot (for clarity/visualization):
                        self.array[self.front] = -1
                      This keeps the convention that -1 represents an empty slot.

                - Step 3: Update indices:
                    - If there was only one element in the queue:
                        - This is detected by:
                            self.front == self.rear
                        - After removing it, the queue becomes empty:
                            - Set:
                                self.front, self.rear = -1, -1
                    - Otherwise (more than one element):
                        - Move the front index forward in a circular manner:
                            self.front = (self.front + 1) % self.get_size()
                        - This uses modular arithmetic to wrap around to the
                          beginning of the array when the end is reached.

                - Step 4: Return the removed value:
                    - Return data.

            Invariants relied upon:
                - An empty queue has:
                    - self.front == -1 and self.rear == -1
                - When the queue has elements:
                    - self.front points to the oldest element (front of the queue).
                    - self.rear points to the most recently inserted element.
                - Circular movement (wrap-around) is always done using:
                    (index + 1) % self.get_size()

        Time Complexity:
            - O(1), since it performs a constant number of array accesses
              and arithmetic operations.

        Space Complexity:
            - O(1), as it uses only existing attributes and one local
              variable (`data`).
        """
        if self.is_empty():
            print("Queue is empty")
            return
        
        data = self.array[self.front]
        self.array[self.front] = -1
        
        if self.front == self.rear:
            self.front, self.rear = -1, -1
        else:
            self.front = (self.front + 1) % self.get_size()
            
        return data    
        