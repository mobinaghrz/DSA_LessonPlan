class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
        
class PriorityQueue:
    def __init__(self):
        self.head = None 
        
    def insert(self, data):
        """
        Input:
            - data: The value to be inserted into the linked list while
                    maintaining the list's sorted order.

        Output:
            - None (the method modifies the linked list in place).

        Description:
            The insert method adds a new node containing `data` into a
            sorted singly linked list, ensuring the list remains ordered
            after insertion.

            Sorting Rule:
                - The list is maintained in **non-increasing order**
                (i.e., each node's data is >= the data of the next node).

            Process:
                - Step 1: Create a new node:
                    - new_node = Node(data)

                - Step 2: Check if insertion occurs at the head:
                    - If the list is empty (self.head is None), OR
                    - If the new data is greater than the current head’s data:
                        - Set:
                            new_node.next = self.head
                            self.head = new_node
                        - Return immediately, as insertion is complete.

                - Step 3: Traverse the list to find the correct position:
                    - Use a pointer `current` starting at the head.
                    - Continue traversal while:
                        - current.next is not None, and
                        - current.next.data >= data
                    - This ensures that the new node is inserted just after
                    the last node whose value is >= the new data.

                - Step 4: Insert the new node:
                    - Link the new node into the list by:
                        new_node.next = current.next
                        current.next = new_node

                - Step 5: Reset or adjust size tracking (if applicable):
                    - The provided code sets:
                        self.size = 0
                    (This appears to reset a size counter rather than update it;
                    ensure this behavior is intentional.)

            Invariants relied upon:
                - The linked list is always kept in descending sorted order.
                - Each node’s `next` pointer correctly links to the following node.
                - The head pointer always references the first (largest) element.

        Time Complexity:
            - O(n), since in the worst case the method may traverse the entire list
            to locate the correct insertion point.

        Space Complexity:
            - O(1), as only one new node and a small number of pointers are used.
        """
        new_node = Node(data)
        
        if self.head is None or self.head.data > data:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        while current.next is not None and current.next.data >= data:
            current = current.next
            
        new_node.next = current.next
        current.next = new_node