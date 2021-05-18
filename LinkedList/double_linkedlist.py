class Node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
    # append the element
    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None
    # prepend the element
    # def prepend(self, data):
    #     if self.head is None:
    #         new_node = Node(data)
    #         new_node.prev = None 
    #         self.head = new_node
    #     else:
    #         new_node = Node(data)
    #         self.head.prev = new_node
    #         new_node.next = self.head
    #         self.head = new_node
    #         new_node.prev = None

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

if __name__ == "__main__":
    dllist = DoublyLinkedList()
    # dllist.prepend(0)
    dllist.append(1)
    dllist.append(2)
    dllist.append(3)
    dllist.append(4)
    # dllist.prepend(5)

    dllist.print_list()