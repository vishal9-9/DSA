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
