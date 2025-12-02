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
        itr = self.head
        while itr is not None:
            if itr.data == aim:
                print("Found it!")
                break
            itr = itr.next
            
    def add_first(self, value):
        """
        Input:
            - value: the data to be stored in the new node added
                    at the beginning of the linked list

        Output:
            - void (updates the linked list by inserting a new node at the head)

        Description:
            The addFirst method inserts a new node containing the given value
            at the beginning (head) of the linked list.

            Process:
                - Create a new Node with the provided value.
                - If the list is empty (head is None):
                    - Set both head and tail to the new node.
                - Otherwise:
                    - Set newNode.next to point to the current head.
                    - Update head so that it becomes the new node.
                - Increase the size of the list by 1.

            This method ensures constant-time insertion at the start of the list.

        Time Complexity:
            - O(1), insertion at the head requires no traversal

        Space Complexity:
            - O(1), only one additional node reference is created
        """
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

        self.size += 1  

