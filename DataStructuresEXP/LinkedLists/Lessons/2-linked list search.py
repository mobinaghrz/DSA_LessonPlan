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
        itr = self.head
        while itr is not None:
            print(itr.data)
            itr = itr.next
            
    def search(self, aim):
        """
        Input:
            - aim: the value to search for within the linked list

        Output:
            - void (prints "Found it!" if the value is located)

        Description:
            The search method scans through the linked list starting
            from the head and checks each node's data to determine
            whether it matches the target value ('aim').

            Process:
                - Initialize a pointer (itr) to the head of the list
                - While itr is not None:
                    - Compare itr.data with the aim value
                    - If a match is found:
                        - Print "Found it!"
                        - Break out of the loop (search ends)
                    - Otherwise, move to the next node

            This method performs a linear search through the linked list.
            If the value exists anywhere in the list, the method reports it.
            If the end of the list is reached without finding the value,
            the method simply finishes without printing anything.

        Time Complexity:
            - Worst case: O(n), must potentially scan the entire list
            - Best case:  O(1), if the target is at the head
        
        Space Complexity:
            - O(1), uses only a single pointer regardless of list size
        """
        itr = self.head
        while itr is not None:
            if itr.data == aim:
                print("Found it!")
                break
            itr = itr.next
