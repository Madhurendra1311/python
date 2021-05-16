class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    # function is used to append an value on the top of the stack.
    def push(self, data):
        if self.top is None:
            self.top = Node(data, None)
            return
        self.top = Node(data, self.top)

    # function is used to remove an value from the top of the stack.
    def pop(self):
        if self.top is None:
            return
        temp = self.top
        if self.top is not None:
            self.top = self.top.next
        temp.next = None
        return temp.data

    # function returns the value on the top of the stack.
    def peek(self):
        return self.top.data

    # function simply clears the whole stack.
    def clearstack(self):
        self.top = None

    # if the stack is empty.
    def emptystack(self):
        if self.top is None:
            return True
        return False

    # function is used print out the stacks.
    def display(self):
        iteration = self.top
        linkedStr = ''
        while iteration:
            linkedStr += str(iteration.data) + '-->'
            iteration = iteration.next
        print(linkedStr)
    
if __name__ == "__main__":
    stack = Stack()
    stack.push(20)
    stack.push(10)
    stack.push(40)
    stack.push(50)
    stack.peek()
    stack.display()
    stack.pop()
    stack.push(60)
    stack.display()
    stack.clearstack()