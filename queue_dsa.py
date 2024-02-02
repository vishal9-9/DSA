class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class Queue:
    def __init__(self) -> None:
        self.left = self.right = None

    def enqueue(self, val):
        node = ListNode(val=val)

        if not self.right:
            self.left = self.right = node
        else:
            self.right.next = node
            self.right = self.right.next

    def dequeue(self):
        if not self.left:
            return None

        val = self.left.val
        self.left = self.left.next
        return val

    def show(self):
        cur = self.left
        data = ""
        while cur:
            data += str(cur.val) + " +> "
            cur = cur.next
        return data


if __name__ == "__main__":
    obj = Queue()
    obj.enqueue(1)
    obj.enqueue(2)
    obj.enqueue(3)
    obj.enqueue(4)

    print(obj.show())

    obj.dequeue()
    obj.dequeue()

    print(obj.show())
