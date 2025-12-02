class Node:
    def __init__(self, data, nextNode=None):
        self.data = data
        self.next = nextNode
        

class LinkedList:
    def __init__(self, node=None):
        self.head = node 
        self.tail = node 
        self.size = 0 if self.head is None else 1
        
    def traverse(self):
        """
        Input:
            - self: the LinkedList instance on which the method is called

        Output:
            - void (prints each element of the linked list)

        Description:
            The traverse method iterates through the linked list starting
            from the head node and prints the data stored in each node.

            Process:
                - Begin at the head of the list
                - While the current node is not None:
                    - Print the current node's data
                    - Move to the next node using the 'next' reference

            This method is useful for visualizing or debugging the current
            state of the linked list, as it displays each element in the
            order they appear.

        Time Complexity:
            - O(n), where n is the number of nodes in the linked list.
            Each node is visited exactly once.

        Space Complexity:
            - O(1), as only a single pointer (itr) is used regardless
            of the list size.
        """
        itr = self.head
        while itr is not None:
            print(itr.data)
            itr = itr.next
            