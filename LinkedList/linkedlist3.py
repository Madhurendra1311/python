class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

# Print the linked list
    def listprint(self):
        printval = self.head
        while printval is not None:
            print (printval.data)
            printval = printval.next
    def AtBegining(self,newdata):
        NewNode = Node(newdata)

# Update the new nodes next val to existing node
        NewNode.next = self.head
        self.head = NewNode

list = LinkedList()
list.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list.head.next = e2
e2.next = e3

list.AtBegining("Sun")

list.listprint()