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
        """
        Input:
            - None (operates directly on the internal array and indices)

        Output:
            - The value removed from the front of the queue.

        Description:
            The dequeue method removes and returns the element at the front
            of the queue. The queue is implemented using a fixed-size array
            with two indices:
                - `front` pointing to the first (oldest) element
                - `back` pointing to the last (newest) element

            Process:
                - If the queue is empty (front == -1 and back == -1):
                    - Raise an exception because there is no element to remove.
                - Store the element at `array[front]` in a temporary variable
                  (`to_dequeue`) so it can be returned later.
                - If the queue contains only one element (front == back):
                    - Set both `front` and `back` to -1 to mark the queue
                      as empty.
                    - Return the stored value (`to_dequeue`).
                - Otherwise (there is more than one element):
                    - Shift all elements one position to the left to keep the
                      front of the queue at index 0:
                        - For each index i from 1 up to and including `back`:
                            - Move element at `array[i]` to `array[i - 1]`.
                    - After shifting, clear the slot that used to hold the last
                      element:
                        - Set `array[back]` to 0 (optional, for cleanliness).
                    - Decrease `back` by 1 because the queue now has one fewer
                      element.
                    - Keep `front` at 0, since the front element now resides
                      at index 0 after shifting.
                - Return the stored value (`to_dequeue`).

            This method maintains a simple, non-circular array-based queue
            by always keeping the front at index 0 and shifting all elements
            left after each dequeue.

        Time Complexity:
            - O(n), where n is the current number of elements in the queue,
              due to the shifting of elements after removing the front.

        Space Complexity:
            - O(1), no additional significant memory is allocated; the method
              operates in place on the existing array.
        """
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