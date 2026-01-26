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
        """
        Input:
            - None (operates directly on the queue's internal state).

        Output:
            - bool:
                - True  -> if the circular queue is full.
                - False -> otherwise.

        Description:
            The is_full method checks whether the circular queue has reached
            its maximum capacity and cannot accept any more elements.

            Process:
                - It uses the standard circular queue fullness condition:
                    (rear + 1) % size == front

                - Here:
                    - `rear` is the index of the last (most recently added)
                      element in the queue.
                    - `front` is the index of the first (oldest) element in
                      the queue.
                    - `size` is the total capacity of the underlying array,
                      obtained via `self.get_size()`.

                - Intuition:
                    - In a circular queue, `rear` moves forward (with wrap-around)
                      when elements are enqueued:
                          rear = (rear + 1) % size
                    - The queue is considered **full** when advancing `rear`
                      by one position (with wrap-around) would make it equal
                      to `front`. That means there is no free slot left.

                - Special cases:
                    - When the queue is empty:
                        - `front == -1` and `rear == -1`
                        - The expression:
                            (rear + 1) % size == front
                          becomes:
                            ( -1 + 1 ) % size == -1
                            0 == -1  -> False
                          so an empty queue is correctly reported as not full.

            Correctness Conditions:
                - This condition is correct **provided that**:
                    - `self.get_size()` returns the length of the underlying
                      array (i.e., the queue's capacity).
                    - `front` and `rear` are updated consistently in your
                      enqueue and dequeue methods, following the circular
                      queue logic:
                        - Enqueue (non-empty):
                            rear = (rear + 1) % size
                        - Dequeue (more than one element):
                            front = (front + 1) % size
                        - When the queue becomes empty:
                            front = rear = -1

        Time Complexity:
            - O(1), since it performs a constant number of arithmetic and
              comparison operations.

        Space Complexity:
            - O(1), as no additional memory is allocated.
        """
        return (self.rear + 1) % self.get_size() == self.front