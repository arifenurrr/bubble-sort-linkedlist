class Node:
    def _init_(self, data):
        self.data = data
        self.next = None


class LLNode:
    def _init_(self, node:Node):
        self.node = node  
        self.next = None  

class LinkedList:
    def _init_(self):
        self.head = None
        self.num_items = 0


    def add_node(self, node, index=None):
        if index is None:  # Default case: Add to the end
            if self.num_items == 0:
                self.head = node
            else:
                temp_node = self.head
                for _ in range(self.num_items - 1):
                    temp_node = temp_node.next
                temp_node.next = node
            self.num_items += 1
            return
        
        if index < 0 or index > self.num_items:  # Invalid index
            raise IndexError("Index out of bounds")
        
        if index == 0:  # Insert at the beginning
            node.next = self.head
            self.head = node
        else:  # Insert at a specific position
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            node.next = temp_node.next
            temp_node.next = node

        self.num_items += 1


    def print_all_nodes(self):
        temp_node = self.head
        for i in range(self.num_items):
            print(temp_node.data)
            temp_node = temp_node.next

    def remove_node(self, index):
        if(self.num_items == 0):
            print("Cannot remove from an empty LL!")
            return
        elif (self.num_items <= index):
            print("LL has {} items cannot remove index {}".format(self.num_items, index))
            return
        elif (index == 0):
            self.head = self.head.next
            self.num_items -= 1
        else:
            temp_node = self.head
            prev = self.head
            for i in range(index-1):
                prev = prev.next
                
            temp_node = prev.next
            prev.next = temp_node.next
            temp_node.next = None
            self.num_items -= 1

def convert_to_linked_list(sequence):
    l1 = LinkedList()
    for i in range(len(sequence)):
        l1.add_node(Node(sequence[i]))
    return l1

class Stack:
    def _init_(self):
        self.top = LinkedList()
        
    def push(self, node):
        self.top.add_node(node, 0)
    
    def peek(self):
        if(self.top.num_items>0):
            return self.top.head.data
        else:
            return "Empty stack"
    
    def pop(self):
        if(self.top.num_items > 0):
            popped_node = self.top.head
            self.top.remove_node(0)
            return popped_node
        else:
            return "Cannot pop from an empty stack"
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

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def get_node(self, index):
        current = self.head
        for _ in range(index):
            if current is None:
                return None
            current = current.next
        return current

    def swap(self, index1, index2):
        node1 = self.get_node(index1)
        node2 = self.get_node(index2)
        if node1 and node2:
            node1.data, node2.data = node2.data, node1.data

    def swap_nodes(self, node1, node2):
       if node1 is None or node2 is None:
        return
        node1.data, node2.data = node2.data, node1.data



def to_list(self):
    result = []
    current = self.head
    while current:
        result.append(current.data)
        current = current.next
    return result


###git 




    


