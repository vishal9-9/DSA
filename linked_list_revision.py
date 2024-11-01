class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head

    def addAtEnd(self, val):
        # Here we need to consider that all elements are added at end so we need to use tail.next
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def remove(self, index):
        i = 0
        cur = self.head
        while cur and i < index:
            i += 1
            cur = cur.next

        if cur:
            cur.next = cur.next.next

    def print(self):
        cur = self.head.next
        while cur:
            print(cur.val)
            cur = cur.next


if __name__ == "__main__":
    obj = LinkedList()
    obj.addAtEnd(1)
    obj.addAtEnd(2)
    obj.addAtEnd(3)
    obj.addAtEnd(4)
    obj.addAtEnd(5)

    obj.print()

    obj.remove(1)
    obj.remove(3)

    obj.print()
