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
        
    def peek(self):
        """
        Input:
            - None (operates directly on the linked list–based queue structure)

        Output:
            - The data stored in the node at the front of the queue (without
            removing that node).

        Description:
            The peek method returns the value at the front of the queue
            without modifying the queue itself.

            Process:
                - If the queue is empty (is_empty() is True):
                    - Raise an exception because there is no element to inspect.
                - Otherwise:
                    - Access the node referenced by `front`.
                    - Return the `data` stored in this front node.
                - The internal structure of the queue (front, back, links, size)
                remains unchanged.

            This method is useful when you need to see which element would be
            removed next by dequeue, while leaving the queue intact.

        Time Complexity:
            - O(1), only a single pointer dereference is performed.

        Space Complexity:
            - O(1), no additional significant memory is used.
        """
        if self.is_empty():
            raise Exception("Queue is empty")
        
        return self.front.data
        