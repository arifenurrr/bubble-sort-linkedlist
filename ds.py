class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def swap_nodes(self, prev, curr):
        nxt = curr.next
        if not nxt:
            return
        curr.next, nxt.next = nxt.next, curr
        if prev:
            prev.next = nxt
        else:
            self.head = nxt


    


