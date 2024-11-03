class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def insert(root: TreeNode, val: int):
    if not root:
        return TreeNode(val)

    if root.val < val:
        return insert(root.right, val)
    elif root.val > val:
        return insert(root.left, val)
    else:
        return root


def minNodeValue(root: TreeNode):
    cur = root
    while cur and cur.left:
        cur = cur.left
    return cur


def remove(root: TreeNode, val: int):
    if not root:
        return None

    if root.val < val:
        return remove(root.right, val)
    elif root.val > val:
        return remove(root.left, val)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            minNode = minNodeValue(root.right)
            root.val = minNode.val
            root.right = remove(root.right, minNode.val)
    return root


def search(root: TreeNode, target: int):
    if not root:
        return False

    if root.val < target:
        return search(root.right, target)
    elif root.val > target:
        return search(root.left, target)
    else:
        return True


def inorder(root: TreeNode):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)


def preorder(root: TreeNode):
    if not root:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)


def postorder(root: TreeNode):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)


from collections import deque


def bfs(root: TreeNode):
    queue = deque()

    if root:
        queue.append(root)

    level = 0
    while len(queue) > 0:
        print("level: ", level)
        for i in range(len(queue)):
            curr = queue.popleft()
            print(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        level += 1
