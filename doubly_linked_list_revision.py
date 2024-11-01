class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertFront(self, val):
        newNode = Node(val)

        # Connected new node to head & node next to head
        newNode.prev = self.head
        newNode.next = self.head.next

        # Removing Previous connection of head & node next to head
        self.head.next.prev = newNode
        self.head.next = newNode

    def insertEnd(self, val):
        newNode = Node(val)

        # Connected new node to tail & node prev to tail
        newNode.prev = self.tail.prev
        newNode.next = self.tail

        # Removing Previous connection of tail & node prev to tail
        self.tail.prev.next = newNode
        self.tail.prev = newNode

    def removeFront(self):
        self.head.next = self.head.next.next
        self.head.next.prev = self.head

    def removeEnd(self):
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail

        # Found New way in removeFront, removeEnd commented old way.

        # self.tail.prev.prev.next = self.tail
        # self.tail.prev = self.tail.prev.prev

    def print(self):
        cur = self.head.next
        while cur != self.tail:
            print(cur.val)
            cur = cur.next


if __name__ == "__main__":
    obj = LinkedList()
    obj.insertFront(4)
    obj.insertFront(3)
    obj.insertFront(2)
    obj.insertFront(1)
    obj.insertEnd(5)
    obj.insertEnd(6)
    obj.insertEnd(7)

    obj.print()

    print()

    obj.removeFront()
    obj.removeFront()
    obj.removeEnd()

    obj.print()
