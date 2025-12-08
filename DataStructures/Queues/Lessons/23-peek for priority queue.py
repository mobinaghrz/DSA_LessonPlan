class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
        
class PriorityQueue:
    def __init__(self):
        self.head = None 
        
    def insert(self, data):
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
        
    def delete_max(self):
        if self.head is None:
            raise Exception("Queue is empty")
        
        max_node = self.head 
        self.head = self.head.next
        
        max_node.next = None 
        
        return max_node.data
    
    def peek(self):
        """
        Input:
            - None (operates directly on the linked list's internal state).

        Output:
            - The maximum value currently stored at the front of the list.
            - If the list is empty:
                - Raises an Exception with message "Queue is empty".

        Description:
            The peek method returns the maximum element in the sorted
            linked list **without removing it**. Because the list is
            maintained in non-increasing order, the maximum value is always
            located at the head.

            Process:
                - Step 1: Check if the list is empty:
                    - If self.head is None:
                        - Raise Exception("Queue is empty")
                        - No further steps are performed.

                - Step 2: Access the maximum value:
                    - The value stored at:
                        self.head.data
                    is the maximum element in the structure.

                - Step 3: Return the value:
                    - The method returns the head’s data without modifying
                    any nodes or pointers.

            Invariants relied upon:
                - The linked list is sorted in descending order.
                - The head always contains the maximum element.
                - No structural changes occur during peek.

        Time Complexity:
            - O(1), since the head node is accessed directly.

        Space Complexity:
            - O(1), using no additional memory beyond a constant reference.
        """
        if self.head is None:
            raise Exception("Queue is empty")
        
        return self.head.data