class ListNode:
    def __init__(self, val) -> None:
        self.prev = None
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_front(self, val):
        node = ListNode(val=val)
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def add_end(self, val):
        node = ListNode(val=val)
        node.next = self.tail
        node.prev = self.tail.prev

        self.tail.prev.next = node
        self.tail.prev = node

    def show(self):
        cur = self.head.next
        while cur != self.tail:
            print(cur.val, " => ", end="")
            cur = cur.next


if __name__ == "__main__":
    obj = LinkedList()
    obj.add_front(1)
    obj.add_front(2)
    obj.add_front(3)
    obj.add_front(4)
    obj.add_end(5)
    obj.add_end(6)
    obj.add_end(7)

    obj.show()
