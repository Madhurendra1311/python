class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
# 1)
     #print the linked_list   

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        iteration = self.head

         # print value variable
        linkedStr = ''                
        while iteration:
            linkedStr += str(iteration.data)+' --> ' if iteration.next else str(iteration.data)
            iteration = iteration.next
        print(linkedStr)

# 2)
    # length of the linked_list   

    def get_length(self):                  
        count = 0
        iteration = self.head
        while iteration:
            count+=1
            iteration = iteration.next

        return count

     #insert the node at beginning   

# 3)
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

# 4)
    def insert_at_end(self, data):
        if self.head is None:                  # if linked_list is blank
            self.head = Node(data, None)
            return

        iteration = self.head

        while iteration.next:                    # if linked_list is not blank
            iteration = iteration.next

        iteration.next = Node(data, None)

# 5)
    # insert the node at middle of the linked_list

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        iteration = self.head
        while iteration:
            if count == index - 1:
                node = Node(data, iteration.next)
                iteration.next = node
                break

            iteration = iteration.next
            count += 1

# 6)
    #delete the node from the linked_list        

    def remove_at(self, index):
        if index<0 or index>=self.get_length():           
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        iteration = self.head
        while iteration:
            if count == index - 1:
                iteration.next = iteration.next.next
                break

            iteration = iteration.next
            count+=1

# 7)
    #add multiple values at the end of the node
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

# 8)
    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        if self.head is None:
            return

        if self.head.data==data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return
        # Now insert data_to_insert after data_after node
        iteration = self.head
        while iteration:
            if iteration.data == data_after:
                iteration.next = Node(data_to_insert, iteration.next)
                break

            iteration = iteration.next

# # 0)
#     def insert_before_value(self, data_before, data_to_insert):
#         # Search for first occurance of data_after value in linked list
#         if self.head is None:
#             return

#         if self.head.data==data_before:
#             return self.insert_at_begining(data_to_insert)
#         # Now insert data_to_insert before data_after node
#         iteration = self.head
#         while iteration:
#             if iteration.data == data_before:
#                 iteration.next = data_to_insert
#                 data_to_insert.next = Node(data_to_insert, iteration.next)
#                 return

#             iteration = Node(data_to_insert, iteration.next)

# 9)
    def remove_by_value(self, data):
        # Remove first node that contains data
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        iteration = self.head
        while iteration.next:
            if iteration.next.data == data:
                iteration.next = iteration.next.next
                break
            iteration = iteration.next

# 10)
    def reverseList(self):
        # initialize variables
        previous = None         # `previous` initially points to None
        current = self.head     # `current` points at the first element
        following = current.next    # `following` points at the second element

        # go till the last element of the list
        while current:
            current.next = previous # reverse the link
            previous = current      # move `previous` one step ahead
            current = following         # move `current` one step ahead
            if following:               # if this was not the last element
                following = following.next    # move `following` one step ahead

        self.head = previous

# 11)
    def replace(self, old_item, new_item):
        # Replace the given old_item in this linked list with given new_item
        if old_item == new_item:
            return
        iteration = self.head
        while iteration is not None:
            if iteration.data == old_item:
                iteration.data = new_item
                return
            iteration = iteration.next
        raise ValueError('Item not found: {}')


if __name__ == '__main__':
    ll = LinkedList()
    # ll.insert_at_begining(5)
    # ll.insert_at_begining(10)
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.insert_at(1,"tomato")
    ll.insert_at(2,"jackFruit")
    # ll.insert_after_value("mango","apple")
    # ll.insert_before_value("mango","aam")
    # ll.remove_by_value("orange")
    # ll.reverseList()
    # ll.remove_at(2)
    # ll.print()

    # ll.insert_values([45,7,12,567,99])
    # ll.insert_at_end(75)
    print(ll.get_length())
    ll.replace('mango', 'aam')
    ll.print()