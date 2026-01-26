class Node:
    def __init__(self, data):
        """
        Input:
            - data: The value to be stored in this node.

        Output:
            - None (initializes a node for use in a linked list)

        Description:
            The __init__ method creates a new node for a singly linked list.

            Process:
                - Store the given `data` in the node’s `data` attribute.
                - Initialize the `next` reference to None, indicating that
                  this node does not yet point to any other node.
                - Later, `next` can be updated to point to another Node
                  when the node is linked into a list or queue.

            This node structure is typically used as the building block for
            linked list–based data structures such as queues, stacks, or
            general linked lists.

        Time Complexity:
            - O(1), constant-time assignments.

        Space Complexity:
            - O(1), each node stores a fixed amount of data and one pointer.
        """
        self.data = data
        self.next = None
        self.prev = None

        
class Queue:
    def __init__(self):
        """
        Input:
            - None (initializes an empty queue)

        Output:
            - None (sets up the internal pointers and size counter)

        Description:
            The __init__ method initializes an empty queue implemented
            using a singly linked list of Node objects.

            Process:
                - Set `front` to None:
                    - Indicates that there is currently no first element
                      in the queue.
                - Set `back` to None:
                    - Indicates that there is currently no last element
                      in the queue.
                - Set `size` to 0:
                    - Tracks how many elements are stored in the queue.
                    - This will be incremented on enqueue and decremented
                      on dequeue.

            After initialization:
                - The queue is empty.
                - Both `front` and `back` are None.
                - Any attempt to dequeue or peek should typically check
                  for emptiness first.

        Time Complexity:
            - O(1), only a few attribute assignments are performed.

        Space Complexity:
            - O(1), the queue object itself stores only a constant amount
              of metadata; nodes will be added later as elements are enqueued.
        """
        self.front = None 
        self.back = None 
        self.size = 0
