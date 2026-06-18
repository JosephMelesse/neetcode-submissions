class Node:
    def __init__(self, val = None, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        i = 0
        curr = self.head
        while curr:
            if i == index:
                return curr.val
            curr = curr.next 
            i += 1
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head
        new_node = Node(val)
        i = 0
        while curr:
            if i == index:
                bar = curr.prev
                if bar:
                    bar.next = new_node 
                    curr.prev = new_node
                    new_node.prev = bar
                    new_node.next = curr
                else:
                    self.addAtHead(val)
                return 
            curr = curr.next
            i += 1
        if i == index:
            self.addAtTail(val)

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head 
        i = 0
        while curr:
            if i == index:
                foo = curr.next # initialize the next node as foo
                bar = curr.prev # initialize the previous node as bar
                if bar:
                    bar.next = foo # if there exists a node before curr, point it's next pointer to foo
                else:
                    self.head = foo # if there is no node before curr, point the head to foo because curr will get garb collected 
                if foo:
                    foo.prev = bar # if there exists a node after curr, point it's prev pointer to bar
                else:
                    self.tail = bar # if there is no node after curr, point the tail to bar because curr will get garb collected 
                return #end the loop
            curr = curr.next # move to the next node
            i += 1 # increment i
                


            


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)