class Node:
    def __init__(self, data):
        """
        Input:
            - data:
                The value stored in this node. In this priority-queue
                implementation, the `data` attribute also represents
                the node’s priority. Higher or lower numerical values
                indicate priority depending on how the PriorityQueue
                handles ordering during insertion.

        Output:
            - None (constructor only initializes internal attributes).

        Description:
            The __init__ method constructs a new node for use in a
            linked-list–based priority queue. Each node stores:
                - The data value, which doubles as the priority.
                - A reference to the next node.

            Process:
                - Step 1: Assign the data/priority value:
                    - Sets:
                        self.data = data
                      This value is used both to store the element and
                      to determine its priority relative to other nodes.

                - Step 2: Initialize the next pointer:
                    - Sets:
                        self.next = None
                      This signifies that the node is not yet linked into
                      the queue. The priority queue will update this field
                      when placing the node in its correct priority position.

            Invariants relied upon:
                - A new node always satisfies:
                    - self.data contains the element’s priority.
                    - self.next is None until linked.
                - In the priority queue:
                    - Node ordering is determined by comparing
                      self.data values across nodes.

        Time Complexity:
            - O(1), since initialization requires only constant-time assignments.

        Space Complexity:
            - O(1), as only the node’s own fields are allocated.
        """
        self.data = data 
        self.next = None 
        
class PriorityQueue:
    def __init__(self):
        """
        Input:
            - None (initializes an empty priority queue).

        Output:
            - None (constructor only sets up internal attributes).

        Description:
            The __init__ method initializes a new PriorityQueue instance
            using a linked-list–based structure. It prepares the internal
            state required for storing and managing nodes according to
            priority-based ordering.

            Process:
                - Step 1: Initialize the head pointer:
                    - Sets:
                        self.head = None
                      This indicates that the queue is currently empty
                      and there is no first (highest-priority) node yet.

                - Step 2: Initialize the tail pointer:
                    - Sets:
                        self.tail = None
                      Since the queue is empty, there is also no last
                      (lowest-priority) node.

                - Step 3: Initialize the size counter:
                    - Sets:
                        self.size = 0
                      This counter tracks the total number of nodes in
                      the priority queue and is incremented/decremented
                      by enqueue/dequeue operations.

            Invariants relied upon:
                - An empty priority queue always satisfies:
                    - self.head is None
                    - self.tail is None
                    - self.size == 0
                - When elements are inserted:
                    - self.head references the node with the highest priority.
                    - self.tail references the node with the lowest priority
                      (depending on implementation of enqueue).
                - self.size always correctly reflects the number of nodes
                  currently stored.

        Time Complexity:
            - O(1), since initialization only involves simple assignments.

        Space Complexity:
            - O(1), because no dynamic structures are allocated beyond
              the three primitive attributes.
        """
        self.head = None 
        self.tail = None 
        self.size = 0