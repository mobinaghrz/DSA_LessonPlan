class Queue:
    def __init__(self, size):
        self.array = ["-"] * size
        self.front = -1
        self.back = -1
        
    def enqueue(self, value):
        if self.back == len(self.array) - 1:
            raise Exception("Queue is full")


        if self.front == -1 and self.back == -1:
            self.front = 0
            self.back = 0
        else:
            self.back += 1

        self.array[self.back] = value


    def dequeue(self):
        if self.front == -1 and self.back == -1:
            raise Exception("Queue is empty")
        
        to_dequeue = self.array[self.front]

        if self.front == self.back:
            self.front = -1
            self.back = -1
            return to_dequeue
        
        for i in range(self.front + 1, self.back + 1):
            self.array[i - 1] = self.array[i]
            
        self.array[self.back] = 0

        self.back -= 1

        return to_dequeue
    
    def is_empty(self):
        """
        Input:
            - None (operates directly on the queue's internal indices)

        Output:
            - bool: True if the queue contains no elements, False otherwise.

        Description:
            The is_empty method checks whether the queue currently holds
            any elements.

            Process:
                - The queue is considered empty when both `front` and `back`
                are set to -1.
                - Return True if `front == -1` and `back == -1`.
                - Otherwise, return False.

            This method relies on the invariant that:
                - When the queue becomes empty (after initialization or after
                removing the last element), both `front` and `back` are reset
                to -1.

        Time Complexity:
            - O(1), only constant-time comparisons are performed.

        Space Complexity:
            - O(1), no additional memory is used.
        """
        return self.front == -1 and self.back == -1

    
    def peek(self):
        """
        Input:
            - None (reads from the current front position of the queue)

        Output:
            - The value stored at the front of the queue (without removing it).

        Description:
            The peek method returns the element at the front of the queue
            without removing it.

            Process:
                - If the queue is empty (front == -1 and back == -1):
                    - Raise an exception because there is no element to inspect.
                - Otherwise:
                    - Return the element at index `front` in the internal array.

            This method is useful when you need to see which element would be
            dequeued next, but you do not want to modify the queue itself.

        Time Complexity:
            - O(1), accesses a single array element by index.

        Space Complexity:
            - O(1), no additional memory is used.
        """
        if self.front == -1 and self.back == -1:
            raise Exception("Queue is empty")
        return self.array[self.front]