class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.parent = None
        self.val = key


def insertIter(root, node):
    if root is None:
        root = node

    count = 0
    curr = root
    parent = None
    while curr is not None:
        parent = curr
        if node.val > curr.val:
            curr = curr.right
        else:
            curr = curr.left
        count += 1

    if node.val > parent.val:
        parent.right = node
        parent.right.parent = parent
    else:
        parent.left = node
        parent.left.parent = parent

    print("bstIt: " + str(count))


def deleteIter(root, val):
    curr = root

    # Find val
    while curr.val != val:
        if val > curr.val:
            curr = curr.right
        else:
            curr = curr.left

    # No right child
    if curr.right is None:
        # Has a left child
        if curr == curr.parent.left:
            curr.parent.left = curr.left
            curr.left.val = None
            curr.left = None
        else:
            curr.parent.left.val = None
            curr.parent.left = None
    else:
        # Has a right child
        # Find node to swap and swap its vals
        nextNode = findNextIter(curr)

        temp = curr.val
        curr.val = nextNode.val
        nextNode.val = temp

        # Find node that we just swapped
        curr = curr.right
        while curr.val != val:
            if val > curr.val:
                curr = curr.right
            else:
                curr = curr.left

        # Delete curr

        # if the node we're deleting has a right child
        if curr.right is not None:
            # replacing left child of parent
            if curr == curr.parent.left:
                curr.parent.left = curr.right
                curr.right.val = None
                curr.right = None
            # replacing right child of parent
            elif curr == curr.parent.right:
                curr.parent.right = curr.right
                curr.right.val = None
                curr.right = None
        # No children
        else:
            # deleting parent's left child
            if curr == curr.parent.left:
                curr.parent.left.val = None
                curr.parent.left = None
            else:
                curr.parent.right.val = None
                curr.parent.right = None


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
