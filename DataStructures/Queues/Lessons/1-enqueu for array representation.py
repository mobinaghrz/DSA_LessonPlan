class Queue:
    def __init__(self, size):
        self.array = [0] * size
        self.front = -1
        self.back = -1
        
    def enqueue(self, value):
        """
        Input:
            - value: The element to be inserted at the back of the queue.

        Output:
            - None (modifies the internal array and queue pointers in place)

        Description:
            The Enqueu method inserts a new element at the back (tail) of the
            queue. The queue is implemented as a fixed-size array with
            `front` and `back` indices:

                - `front` points to the index of the current front element.
                - `back` points to the index of the last (most recently
                  inserted) element.

            Process:
                - Check if the queue is full:
                    - If `back` is already at the last valid index
                      (`len(self.array) - 1`), raise an exception indicating
                      that the queue is full.
                - If the queue is empty (front == -1 and back == -1):
                    - Set both `front` and `back` to 0.
                    - Store `value` at `array[0]`.
                - Otherwise (queue has at least one element):
                    - Increment `back` by 1 to move to the next free position.
                    - Store `value` in `array[back]`.

            Note:
                - This implementation uses a simple linear array. Once `back`
                  reaches the end of the array, no more elements can be
                  enqueued even if earlier elements are dequeued, unless the
                  implementation is extended to a circular buffer.

        Time Complexity:
            - O(1), insertion at the back is done with direct index access
              and no traversal.

        Space Complexity:
            - O(1), no additional significant memory is allocated beyond
              the already existing array.
        """
        if self.back == len(self.array) - 1:
            raise Exception("Queue is full")


        if self.front == -1 and self.back == -1:
            self.front = 0
            self.back = 0
        else:
            self.back += 1

        self.array[self.back] = value
