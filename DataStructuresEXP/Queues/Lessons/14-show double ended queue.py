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
    
    def show(self):
        """
        Input:
            - None (operates directly on the queue's internal state).

        Output:
            - None (prints the contents of the queue to the console).

        Description:
            The show method displays all elements in the doubly-ended queue
            from front to back.

            Process:
                - If the queue is empty (is_empty() is True):
                    - Print "Queue is empty".
                    - Return immediately; no further processing is done.
                - Otherwise:
                    - Initialize an iterator variable `itr` to the `front` node.
                    - Traverse the queue from `front` to `back`:
                        - While `itr` is not the `back` node:
                            - Print `itr.data` followed by " <=>", without ending
                            the line (using end=" ").
                            - Move `itr` to the next node: `itr = itr.next`.
                        - After the loop, `itr` references the `back` node:
                            - Print `itr.data` (the last element) with a newline.

            This method relies on the invariants that:
                - `front` points to the first node when the queue is non-empty.
                - `back` points to the last node when the queue is non-empty.
                - Each node's `next` reference correctly links to the following node,
                eventually reaching `back`.

        Time Complexity:
            - O(n), where n is the number of elements in the queue, because each
            node is visited exactly once.

        Space Complexity:
            - O(1), only a single iterator reference (`itr`) is used regardless of
            the queue size.
        """
        if self.is_empty():
            print("Queue is empty")
            return
        
        itr = self.front

        while itr is not self.back:
            print(f"{itr.data} <=>", end=" ")
            itr = itr.next

        print(f"{itr.data}")
