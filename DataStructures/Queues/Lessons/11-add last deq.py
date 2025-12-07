class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 
        self.prev = None

class DoublyEndedQueue:
    def __init__(self):
        self.front = None 
        self.back = None
        self.size = 0

    def is_empty(self):
        """
        Input:
            - None (operates directly on the queue's `front` and `back` attributes)

        Output:
            - bool: True if the queue contains no elements, False otherwise.

        Description:
            The is_empty method checks whether the queue currently holds
            any elements.

            Process:
                - The queue is considered empty when:
                    - `front` is None, and
                    - `back` is None.
                - Return True if both `front` and `back` are None.
                - Otherwise, return False, indicating there is at least one element
                in the queue.

            This method relies on the invariant that:
                - When the first element is added:
                    - Both `front` and `back` reference the same Node.
                - When the last element is removed:
                    - Both `front` and `back` are reset to None.
                - Whenever the queue is non-empty:
                    - `front` and `back` both reference valid Node instances.

        Time Complexity:
            - O(1), a constant-time check of two references.

        Space Complexity:
            - O(1), no additional memory is used.
        """
        return self.front is None and self.back is None
            

    def add_first(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.front = new_node
            self.back = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node

        self.size += 1

    def add_last(self, data):
        """
        Input:
            - data: The value to be stored in the new back node of the queue.

        Output:
            - None (modifies the internal state of the queue in-place).

        Description:
            The add_last method inserts a new element at the back of the
            doubly-ended queue.

            Process:
                - Create a new Node instance containing the given `data`.
                - If the queue is empty (is_empty() is True):
                    - Set both `front` and `back` to reference the new node,
                    since it becomes the only element.
                - Otherwise (queue is non-empty):
                    - Link the new node after the current `back` node:
                        - Set new_node.prev to the current `back`.
                        - Set current `back`.next to new_node.
                    - Update `back` to reference the new node.
                - Increment `size` by 1 to reflect the newly added element.

            This method maintains the invariants:
                - `front` always points to the first node in the queue.
                - `back` always points to the last node in the queue.
                - The node sequence is correctly doubly linked:
                    - Each node (except the first) has a valid `prev`.
                    - Each node (except the last) has a valid `next`.
                - `size` accurately tracks the number of nodes:
                    - Increased by 1 on every successful call to add_last.

        Time Complexity:
            - O(1), all operations are simple pointer updates and an integer increment.

        Space Complexity:
            - O(1) additional space for the new Node reference.
            (The node itself also occupies O(1) space.)
        """
        new_node = Node(data)

        if self.is_empty():
            self.front = new_node
            self.back = new_node
        else:
            new_node.prev = self.back
            self.back.next = new_node
            self.back = new_node

        self.size += 1