class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

        
class Queue:
    def __init__(self):
        self.front = None 
        self.back = None 
        self.size = 0
      
    def is_empty(self):
        """
        Input:
            - None (operates directly on the queue's size attribute)

        Output:
            - bool: True if the queue contains no elements, False otherwise.

        Description:
            The is_empty method checks whether the queue currently holds
            any elements.

            Process:
                - The queue tracks the number of elements using the `size`
                attribute.
                - If `size` is 0, the queue is empty; return True.
                - Otherwise, the queue has one or more elements; return False.

            This method relies on the invariant that:
                - `size` is incremented by 1 every time an element is enqueued.
                - `size` is decremented by 1 every time an element is dequeued.

        Time Complexity:
            - O(1), a single integer comparison.

        Space Complexity:
            - O(1), no additional memory is used.
        """
        return self.size == 0
    
        
    def enqueue(self, data):
        """
        Input:
            - data: The value to be inserted at the back of the queue.

        Output:
            - None (modifies the queue's internal linked structure in place)

        Description:
            The enqueue method inserts a new element at the back (tail) of
            the queue. The queue is implemented as a doubly linked list of
            Node objects, tracked by `front` and `back` pointers:

                - `front` points to the first node in the queue
                (the next one to be dequeued).
                - `back` points to the last node in the queue
                (the most recently enqueued).

            Process:
                - Create a new Node containing the given `data`.
                - If the queue is empty (size == 0):
                    - Set both `front` and `back` to reference this new node,
                    since it is now the only element in the queue.
                - Otherwise (the queue already has at least one node):
                    - Link the new node after the current `back`:
                        - Set `new_node.prev` to the current `back` node.
                        - Set `back.next` to `new_node` to connect the last node
                        to the new one.
                    - Update `back` to point to `new_node`, making it the new
                    last node in the queue.
                - Increment `size` by 1 to reflect that one more element is
                stored in the queue.

            This method maintains correct forward (`next`) and backward (`prev`)
            links between nodes while efficiently appending at the tail.

        Time Complexity:
            - O(1), insertion at the back uses direct pointer updates.

        Space Complexity:
            - O(1) additional space, aside from the new node created to store
            the enqueued data.
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

                
            