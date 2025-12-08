class CircularQueue:
    def __init__(self, size):
        self.array = [-1] * size
        self.front = -1
        self.rear = -1
        
    def is_empty(self):
        """
        Input:
            - None (operates directly on the queue's internal state).

        Output:
            - bool:
                - True  -> if the circular queue is empty.
                - False -> otherwise.

        Description:
            The is_empty method checks whether the circular queue currently
            contains any elements.

            Process:
                - The queue is considered empty when:
                    - `front == -1` AND `rear == -1`
                - This condition is based on the queue invariant that:
                    - Both `front` and `rear` are initialized to -1 when the
                      queue is created or becomes empty after deletions.
                - The method evaluates this condition:
                    - If both indices are -1:
                        - Return True, indicating the queue has no elements.
                    - Otherwise:
                        - Return False, indicating there is at least one
                          element present in the queue.

            This method does not modify the queue; it only inspects the
            current values of `front` and `rear`.

        Time Complexity:
            - O(1), since it performs a constant-time comparison of two
              integer attributes.

        Space Complexity:
            - O(1), as no additional data structures are used; it only
              reads existing attributes.
        """
        return self.front == -1 and self.rear == -1