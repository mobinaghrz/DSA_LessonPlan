class CircularQueue:
    def __init__(self, size):
        """
        Input:
            - size (int):
                The maximum number of elements that the circular queue
                can hold. This determines the fixed capacity of the
                underlying array.

        Output:
            - None

        Description:
            The constructor initializes an empty circular queue with a
            fixed capacity defined by `size`.

            Process:
                - Create an internal array `self.array` of length `size`:
                    - All positions are initialized to -1 to indicate
                      that they are currently empty.
                - Initialize two index pointers:
                    - `self.front`:
                        - Set to -1 to indicate that the queue is empty
                          and there is no "front" element yet.
                    - `self.rear`:
                        - Also set to -1 to indicate that no elements
                          have been enqueued and there is no "rear"
                          element yet.

            This setup establishes the initial state for a circular queue:
                - The array will store the actual data elements.
                - `front` will later refer to the index of the first
                  (oldest) element in the queue.
                - `rear` will later refer to the index of the last
                  (most recently added) element in the queue.
                - The circular behavior (wrapping around the array) will
                  typically be handled in enqueue/dequeue operations using
                  modular arithmetic, e.g., (index + 1) % size.

        Time Complexity:
            - O(n), where n is the size of the queue:
                - Initializing the internal array with -1 requires
                  touching each of the `size` positions once.

        Space Complexity:
            - O(n), where n is the size of the queue:
                - The internal array `self.array` stores up to `size`
                  elements.
            - O(1) additional space:
                - Only a constant number of extra variables (`front`,
                  `rear`) are used.
        """
        self.array = [-1] * size
        self.front = -1
        self.rear = -1