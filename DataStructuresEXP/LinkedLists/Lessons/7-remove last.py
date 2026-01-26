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
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

        self.size += 1 
        
    def add_last(self, value):
        newNode = Node(value)

        if self.tail is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

        self.size += 1
        
    def insert(self, value, index):
        if index < 0 or index > self.size:
            raise Exception("index out of range")

        if index == 0:
            self.add_first(value)
            return

        if index == self.size:
            self.add_last(value)
            return

        counter = 0
        prev_node = self.head
        while counter + 1 != index:
            prev_node = prev_node.next
            counter += 1

        newNode = Node(value)
        newNode.next = prev_node.next
        prev_node.next = newNode
        self.size += 1
        
    def remove_first(self):
        if self.head is None:
            raise Exception("linked list is empty")
        elif self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            target = self.head
            self.head = self.head.next
            target.next = None

        self.size -= 1

    def remove_last(self):
        """
        Input:
            - None (operates on the LinkedList instance)

        Output:
            - void (removes the last node from the linked list)

        Description:
            The remove_last method deletes the node at the end (tail) of
            the linked list.

            Process:
                - If the list is empty (head is None):
                    - Raise an exception because there is no node to remove.

                - If the list contains only one node (head is tail):
                    - Set both head and tail to None, making the list empty.

                - If the list contains multiple nodes:
                    - Start at the head and iterate until reaching the node
                    immediately before the tail.
                    - Disconnect the last node by setting the predecessor's
                    next reference to None.
                    - Update the tail pointer so it refers to the predecessor.

                - Decrease the size of the list by 1.

            This method requires traversal to find the node before the tail,
            since a singly linked list does not support backward movement.

        Time Complexity:
            - O(n), because traversal from the head to the second-to-last
            node is required

        Space Complexity:
            - O(1), uses only a single iteration pointer
        """
        if self.head is None:
            raise Exception("linked list is empty")
        elif self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            itr = self.head
            while itr.next is not self.tail:
                itr = itr.next

            itr.next = None
            self.tail = itr

        self.size -= 1