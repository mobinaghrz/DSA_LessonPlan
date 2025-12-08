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
        """
        Input:
            - None (operates directly on the linked list's internal state).

        Output:
            - The maximum value removed from the list.
            - If the list is empty:
                - Raises an Exception with message "Queue is empty".

        Description:
            The delete_max method removes and returns the maximum element
            from a sorted singly linked list. Because the list is maintained
            in **non-increasing order** (largest elements at the front),
            the maximum value is always located at the head.

            Process:
                - Step 1: Check if the list is empty:
                    - If self.head is None:
                        - Raise Exception("Queue is empty")
                        - No further processing is done.

                - Step 2: Identify the maximum element:
                    - The head node holds the maximum value:
                        max_node = self.head

                - Step 3: Remove the maximum node from the list:
                    - Update the head pointer to the next node:
                        self.head = self.head.next
                    - Detach the removed node from the list for safety:
                        max_node.next = None

                - Step 4: Return the maximum value:
                    - Return:
                        max_node.data

            Invariants relied upon:
                - The linked list is sorted in descending order.
                - The head always contains the maximum element.
                - Each node correctly links to the next node in the chain.

        Time Complexity:
            - O(1), because accessing and removing the head of a singly
            linked list requires constant time.

        Space Complexity:
            - O(1), using only a reference to the removed node.
        """
        if self.head is None:
            raise Exception("Queue is empty")
        
        max_node = self.head 
        self.head = self.head.next
        
        max_node.next = None 
        
        return max_node.data