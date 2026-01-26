class MitraNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class MitraLinkedList:
    def __init__(self):
        self.first = MitraNode(None)
        self.last = MitraNode(None)
        
        self.first.next = self.last
        self.last.prev = self.first
        

        self.pointer = self.first

        self.size = 2

    def add(self, data):
        new_node = MitraNode(data)

        new_node.prev = self.pointer
        new_node.next = self.pointer.next

        self.pointer.next.prev = new_node
        self.pointer.next = new_node

        self.pointer = new_node

    def merge(self, size, values):
        for val in values:
            self.add(val)

        self.size += size

    def prev(self):
        if self.pointer is self.first:
            return
        
        self.pointer = self.pointer.prev

    def next(self):
        if self.pointer is self.last:
            return
        
        self.pointer = self.pointer.next


    def remove(self):
        temp = self.pointer

        self.pointer.next.prev = temp.prev
        self.pointer.prev.next = temp.next

        if self.pointer.prev is self.first:
            if self.size == 3:
                self.pointer = self.first
            else:
                self.pointer = temp.next
        else:
            self.pointer = temp.prev


        temp.next = None
        temp.prev = None

        self.size -= 1

    def print(self):
        if self.pointer in [self.first, self.last]:
            print("null")
        else:
            print(self.pointer.data)

    def show_status(self):
        print("first <=>", end=" ")
        itr = self.first.next

        while itr != self.last:
            print(f"{itr.data} <=>", end=" ")
            itr = itr.next

        print("last")

        print(f"pointer: {self.pointer.data}")


operations = int(input())

def solution(ops):
    mll = MitraLinkedList()

    for _ in range(ops):
        op = input()

        if op == "merge":
            size = int(input())
            numbers = list(map(int, input().split()))
            mll.merge(size, numbers)
        elif op == "prev":
            mll.prev()
        elif op == "next":
            mll.next()
        elif op == "remove":
            mll.remove()
        elif op == "print":
            mll.print()
        elif op == "status":
            mll.show_status()

solution(operations)