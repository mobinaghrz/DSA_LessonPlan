class Queue:
    def __init__(self, size):
        """
        Input:
            - size (int): The maximum number of elements that the queue can hold.

        Output:
            - None (initializes the internal array and queue pointers)

        Description:
            The __init__ method initializes a fixed-size queue implemented
            using a Python list.

            Process:
                - Allocate an underlying list `array` of the given size and
                  initialize all positions to 0 (placeholder values).
                - Initialize `front` and `back` indices to -1 to represent
                  an empty queue:
                    - front == -1 and back == -1 means the queue is empty.
                - The queue will grow by moving `back` forward as elements
                  are enqueued. When the first element is added, both
                  `front` and `back` will be set to 0.

            This constructor prepares all internal state needed for queue
            operations such as enqueue and (eventually) dequeue.

        Time Complexity:
            - O(n), where n = size of the queue, due to allocating the list
              of length `size`.

        Space Complexity:
            - O(n), where n = size, for storing the elements of the queue.
        """
        self.array = [0] * size
        self.front = -1
        self.back = -1
                        