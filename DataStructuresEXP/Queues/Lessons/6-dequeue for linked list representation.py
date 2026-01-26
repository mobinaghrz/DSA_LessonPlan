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

        new_node = Node(data)
        
        if self.is_empty():
            self.front = new_node
            self.back = new_node
        else:
            new_node.prev = self.back
            self.back.next = new_node
            self.back = new_node
            
        self.size += 1

    def dequeue(self):
        """
        Input:
            - None (operates directly on the linked list–based queue structure)

        Output:
            - The data stored in the node that was removed from the front
            of the queue.

        Description:
            The dequeue method removes and returns the node at the front
            of the queue. The queue is implemented as a doubly linked list
            with:

                - `front` pointing to the first node (oldest element).
                - `back` pointing to the last node (newest element).
                - `size` tracking the number of elements in the queue.

            Process:
                - If the queue is empty (is_empty() is True):
                    - Raise an exception because there is no element to remove.
                - Store a reference to the current front node in `temp`.
                - If the queue contains only one node (size == 1):
                    - Set both `front` and `back` to None, making the queue empty.
                - Otherwise (size > 1):
                    - Move `front` to the next node:
                        - `front = temp.next`
                    - Disconnect the removed node from the list:
                        - Set `temp.next` to None so it no longer points to
                        the new front.
                        - Set `front.prev` to None so the new front has no
                        previous node.
                - Decrease `size` by 1 to reflect that one element was removed.
                - Return `temp.data`, the value stored in the removed node.

            This method ensures that removal happens from the front of the
            queue (FIFO behavior) and maintains correct forward (`next`) and
            backward (`prev`) links in the doubly linked list.

        Time Complexity:
            - O(1), removal from the front updates only a constant number
            of pointers.

        Space Complexity:
            - O(1), no additional significant memory is used.
        """
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
        
            
        