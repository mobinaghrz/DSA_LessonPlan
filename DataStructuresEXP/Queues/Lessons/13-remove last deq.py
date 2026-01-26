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
        new_node = Node(data)

        if self.is_empty():
            self.front = new_node
            self.back = new_node
        else:
            new_node.prev = self.back
            self.back.next = new_node
            self.back = new_node

        self.size += 1

    def remove_first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        
        temp = self.front

        if self.size == 1:
            self.front = None 
            self.back = None
        else:
            self.front = temp.next

            temp.next = None 
            self.front.prev = None 

        self.size -= 1
        return temp.data

    def remove_last(self):
        """
        Input:
            - None (operates directly on the queue's internal state).

        Output:
            - data: The value stored in the node that was at the back of the queue
                    before removal.

        Description:
            The remove_last method removes the element at the back of the
            doubly-ended queue and returns its value.

            Process:
                - If the queue is empty (is_empty() is True):
                    - Raise an Exception indicating that the queue is empty and
                    no removal can be performed.
                - Store the current `back` node in a temporary variable `temp`.
                - If the queue contains exactly one element (size == 1):
                    - Set `front` to None.
                    - Set `back` to None.
                    - The queue becomes empty.
                - Otherwise (queue has more than one element):
                    - Move `back` to the previous node: `back = temp.prev`.
                    - Detach the old back node:
                        - Set `temp.prev` to None.
                    - Ensure the new `back` node has no next link:
                        - Set `back.next` to None.
                - Decrement `size` by 1 to reflect the removed element.
                - Return `temp.data`, the value stored in the removed back node.

            This method maintains the invariants:
                - When the queue becomes empty after removal:
                    - Both `front` and `back` are None.
                    - `size` is 0.
                - When the queue remains non-empty:
                    - `back` points to the new last node.
                    - `front` still points to the first node, since only the last
                    node was removed.
                    - The new `back` node has `next` set to None.
                - `size` accurately tracks the number of elements, decreasing by 1
                on every successful removal.

        Time Complexity:
            - O(1), all operations are constant-time pointer updates and an integer decrement.

        Space Complexity:
            - O(1), no additional memory is allocated beyond a temporary reference.
        """
        if self.is_empty():
            raise Exception("Queue is empty")
        
        temp = self.back

        if self.size == 1:
            self.front = None 
            self.back = None
        else:
            self.back = temp.prev

            temp.prev = None 
            self.back.next = None 

        self.size -= 1
        return temp.data