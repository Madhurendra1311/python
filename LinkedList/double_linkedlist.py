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
    #prepend the element
    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None 
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None
    #add element after node
    def add_after_node(self, key, data):
        cur = self.head
        while cur:
            if cur.next is None and cur.data == key:
                self.append(data)
            elif cur.data == key:
                new_node = Node(data)
                nxt = cur.next 
                cur.next = new_node
                new_node.next = nxt
                nxt.prev = new_node
            cur = cur.next
    #add element before node
    def add_before_node(self, key, data):
        cur = self.head 
        while cur:
            if cur.prev is None and cur.data == key:
                self.prepend(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                prev = cur.prev
                prev.next = new_node
                cur.prev = new_node
                new_node.next = cur
            cur = cur.next
    #delete the node from various places
    def delete(self, key):
        cur = self.head
        while cur:
            if cur.data == key and cur == self.head:
                # Case 1:
                if not cur.next:
                    cur = None 
                    self.head = None
                    return

                # Case 2:
                else:
                    nxt = cur.next
                    cur.next = None 
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return 

            elif cur.data == key:
                # Case 3:
                if cur.next:
                    nxt = cur.next 
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None 
                    cur.prev = None
                    cur = None
                    return

                # Case 4:
                else:
                    prev = cur.prev 
                    prev.next = None 
                    cur.prev = None 
                    cur = None 
                    return 
            cur = cur.next

    def get_length(self):
        count = 0
        iteration = self.head
        while iteration:
            count += 1
            iteration = iteration.next

        return count

    def reverse(self):
        tmp = None
        cur = self.head
        while cur:
            tmp = cur.prev
            cur.prev = cur.next
            cur.next = tmp
            cur = cur.prev
        if tmp:
            self.head = tmp.prev

    def search_node(self, val_to_search):
        i = 1
        flag_val = False
        curr = self.head
        if self.head is None:
            print("List is empty")
            return
        while(curr != None):
            if(curr.data == val_to_search):
                flag_val = True
                break
            curr = curr.next
            i = i + 1
        if(flag_val):
            print("The node is present in the list at position : ")
            print(i)
        else:
            print("The node isn't present in the list")

    #sortList() will sort the given list in ascending order  
    def sortList(self):  
        #Check whether list is empty  
        if(self.head == None):  
            return
        else:  
            #Current will point to head  
            current = self.head  
            while(current.next != None):  
                #Index will point to node next to current  
                index = current.next
                while(index != None):  
                    #If current's data is greater than index's data, swap the data of current and index  
                    if(current.data > index.data):  
                        temp = current.data
                        current.data = index.data
                        index.data = temp
                    index = index.next  
                current = current.next  


    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

if __name__ == "__main__":
    dllist = DoublyLinkedList()
    dllist.prepend(0)
    dllist.append(1)
    dllist.append(2)
    dllist.append(3)
    dllist.append(4)
    dllist.prepend(5)
    # dllist.add_after_node(3,6)
    # dllist.add_before_node(4,9)
    # dllist.delete(1)
    # dllist.delete(6)
    # dllist.delete(4)

    # dllist.delete(3)
    # print(dllist.get_length())
    # dllist.search_node(5)
    dllist.sortList()
    # dllist.reverse()

    dllist.print_list()