# Linked List


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = Node(-1)
        self.tail = self.head

    def add_node(self, val):
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def remove_node(self, index):
        i = 0
        cur = self.head
        while cur and i < index:
            i += 1
            cur = cur.next

        if cur:
            cur.next = cur.next.next

    def show(self):
        cur = self.head.next
        while cur.next:
            print(cur.val, "-->", end="")
            cur = cur.next
        print(cur.val)


if __name__ == "__main__":
    obj = LinkedList()
    obj.add_node(1)
    obj.add_node(2)
    obj.add_node(3)
    obj.add_node(3)
    obj.add_node(3)
    obj.add_node(3)
    obj.add_node(3)

    obj.show()

    obj.remove_node(6)

    obj.show()
