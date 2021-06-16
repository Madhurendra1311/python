class Node {
    constructor(data, next = null) {
        this.data = data;
        this.next = next;
    }
}

class LinkedList {
    constructor() {
        this.head = null
        this.size = 0
    }
    // 1) insertFirst()

    // Insert Node at first position
    insertFirst(data) {
        this.head = new Node(data, this.head);
        this.size++;
    }

    // 2) insertLast()

    // Insert Node at last position
    insertLast(data) {
        const newLast = new Node(data);

        // Check if list is empty then last node is first node which will be head
        if (!this.head) {
            this.head = newLast;
        }
        else {
            // if list is not empty traverse to last node
            let last = this.head;
            while (last.next) {
                last = last.next;
            }
            last.next = newLast;
        }
        this.size++;
    }

    // 3) insertAt()

    // insert a node at a particular index
    insertAt(data, index) {
        // check if index is valid
        if (index >= 0 && index < this.size) {
            // if first index
            if (index === 0) {
                this.head = new Node(data, this.head);
                return;
            }

            const node = new Node(data);
            let current, previous;

            current = this.head;
            let count = 0;

            while (count < index) {
                previous = current;
                count++;
                current = current.next;
            }

            node.next = current;
            previous.next = node;

            this.size++;
        }
        else {
            console.log('You have entered an invalid index!!');
        }
    }

    // 4) removeAt()

    // remove a  node at a particular index

    removeAt(index) {
        let current = this.head;
        let previous;
        let count = 0;
        // check if index is valid
        if (index >= 0 && index < this.size) {
            // if first index
            if (index === 0) {
                this.head = current.next;
            }
            else {
                while (count < index) {
                    previous = current;
                    current = current.next;
                    count++;
                }
                previous.next = current.next;
            }
            this.size--;
        }
        else {
            console.log('You have entered an invalid index!!');
        }
    }

    // 5) getAt()

    getAt(index) {
        let current = this.head;
        let count = 0;
        // check if index is valid
        if (index >= 0 && index < this.size) {
            // if first index
            if (index === 0) {
                // console.log(this.data);
                return this.head.data;
            }

            while (count != index) {
                current = current.next;
                count++;
            }

            // console.log(current.data);
            return current.data;
        }
        else {
            console.log('You have entered an invalid index!!');
        }
    }

    // 6) clearList()

    // clear a whole list
    clearList() {
        this.head = null;
        this.size = 0;
    }

    // 7) printListData()

    // print all data in list
    printListData() {
        let current = this.head;

        if (!this.head) {
            console.log('The list is empty!!');
            return;
        }

        while (current != null) {
            console.log(current.data);
            current = current.next;
        }
    }

}


const li = new LinkedList();
li.insertLast(200);
li.insertFirst(100);
li.insertAt(300, 1);
li.insertLast(400);
li.printListData();
console.log(`The size of list is ${li.size}`);
console.log(li.getAt(2));
li.removeAt(1);
console.log(`The size of list is ${li.size}`);
li.clearList();
console.log(`The size of list is ${li.size}`);