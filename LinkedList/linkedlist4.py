class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

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

    # length of the linked_list   

    def get_length(self):                  
        count = 0
        iteration = self.head
        while iteration:
            count+=1
            iteration = iteration.next

        return count

     #insert the node at beginning   

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:                  # if linked_list is blank
            self.head = Node(data, None)
            return

        iteration = self.head

        while iteration.next:                    # if linked_list is not blank
            iteration = iteration.next

        iteration.next = Node(data, None)

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

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


if __name__ == '__main__':
    ll = LinkedList()
    # ll.insert_at_begining(5)
    # ll.insert_at_begining(10)
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.insert_at(1,"tomato")
    ll.insert_at(2,"jackFruit")
    # ll.remove_at(2)
    # ll.print()

    # ll.insert_values([45,7,12,567,99])
    # ll.insert_at_end(75)
    print(ll.get_length())
    ll.print()