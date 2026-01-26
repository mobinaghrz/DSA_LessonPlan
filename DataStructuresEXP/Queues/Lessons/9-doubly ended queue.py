class Node:
    def __init__(self, data):
        """
        Input:
            - data: The value to be stored in this node. This can be any Python object.

        Output:
            - None (constructor initializes a new Node instance in-place).

        Description:
            The Node class represents a single element in a doubly linked structure
            used by the DoublyEndedQueue.

            Process:
                - Store the provided `data` in the `data` attribute.
                - Initialize `next` to None, indicating there is no node after this one yet.
                - Initialize `prev` to None, indicating there is no node before this one yet.

            This layout allows each Node to:
                - Link forward to another node via `next`.
                - Link backward to another node via `prev`.
                - Store the payload value in `data`.

        Time Complexity:
            - O(1), simple attribute assignments.

        Space Complexity:
            - O(1) per node, fixed number of attributes regardless of the stored data.
        """
        self.data = data
        self.next = None 
        self.prev = None

class DoublyEndedQueue:
    """
    Input:
        - None (creates an empty doubly-ended queue).

    Output:
        - None (constructor initializes a new DoublyEndedQueue instance in-place).

    Description:
        The DoublyEndedQueue class represents a deque (double-ended queue)
        implemented using a doubly linked structure of Node objects.

        Process:
            - Initialize `front` to None, indicating there is no first element yet.
            - Initialize `back` to None, indicating there is no last element yet.
            - Initialize `size` to 0, because the queue starts empty.

        These attributes are used as follows:
            - `front` points to the first node when the queue is non-empty.
            - `back` points to the last node when the queue is non-empty.
            - `size` tracks how many elements are currently stored in the queue.

        Future enqueue/dequeue operations will:
            - Update `front` and `back` to maintain correct ends of the queue.
            - Increment `size` when elements are added.
            - Decrement `size` when elements are removed.

    Time Complexity:
        - O(1), a constant amount of work to set initial attributes.

    Space Complexity:
        - O(1), only three attributes are allocated regardless of future queue size.
    """
    def __init__(self):
        self.front = None 
        self.back = None
        self.size = 0