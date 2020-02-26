class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.parent = None
        self.val = key


def insertIter(root, node):
    if root is None:
        root = node

    curr = root
    parent = None
    while curr is not None:
        parent = curr
        if node.val > curr.val:
            curr = curr.right
        else:
            curr = curr.left

    if node.val > parent.val:
        parent.right = node
        parent.right.parent = parent
    else:
        parent.left = node
        parent.left.parent = parent


def deleteIter(root, val):
    curr = root

    while curr.val != val:
        if val > curr.val:
            curr = curr.right
        else:
            curr = curr.left

    # One child
    if curr.left is None and curr.right is not None:
        temp = curr.right
        curr.right = None
        return temp
    elif curr.left is not None and curr.right is None:
        temp = curr.left
        curr.left = None
        return temp

    # Two children
    temp = findMinIter(curr.right)
    curr.val = temp.val

    # Delete after swap
    curr = curr.right
    while curr.left is not None:
        curr = curr.left
    curr = None


def findNextIter(node):
    if node.right is not None:
        return findMinIter(node.right)

    curr = node
    while curr.parent.val < node.val:
        curr = curr.parent
        if curr.parent is None:
            return None
    return curr.parent


def findPrevIter(node):
    if node.left is not None:
        return findMaxIter(node.left)

    curr = node
    while curr.parent.val > node.val:
        curr = curr.parent
        if curr.parent is None:
            return None
    return curr.parent


def findMinIter(node):
    curr = node
    while curr.left is not None:
        curr = curr.left
    return curr


def findMaxIter(node):
    curr = node
    while curr.right is not None:
        curr = curr.right
    return curr


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


r = Node(10)
insertIter(r, Node(15))
insertIter(r, Node(2))
insertIter(r, Node(1))
insertIter(r, Node(8))
insertIter(r, Node(12))
insertIter(r, Node(20))
insertIter(r, Node(11))

print(findPrevIter(r.right.right).val)