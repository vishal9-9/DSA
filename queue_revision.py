class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.head = self.tail = None

    def enqueue(self, val):
        # if elements in queue
        if self.tail:
            self.tail.next = Node(val)
            self.tail = self.tail.next
        # if queue is empty
        else:
            self.head = self.tail = Node(val)

    def dequeue(self):
        # if elements in queue
        if self.head:
            to_return = self.head.val
            self.head = self.head.next
            print(to_return)
        # if queue is empty
        else:
            print(None)

    def print(self):
        cur = self.head

        while cur:
            print(cur.val, " -> ", end="")
            cur = cur.next


if __name__ == "__main__":
    obj = Queue()
    obj.enqueue(1)
    obj.enqueue(2)
    obj.enqueue(3)
    obj.enqueue(4)

    print(obj.print())

    obj.dequeue()
    obj.dequeue()

    print(obj.print())
