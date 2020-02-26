class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.parent = None
        self.val = key


def insertRec(root, node):
    if root is None:
        root = node

    if node.val < root.val:
        if root.left is None:
            root.left = node
            root.left.parent = root
        else:
            insertRec(root.left, node)

    if node.val > root.val:
        if root.right is None:
            root.right = node
            root.right.parent = root
        else:
            insertRec(root.right, node)


def deleteRec(root, val):
    if root is None:
        return root

    if val < root.val:
        root.left = deleteRec(root.left, val)
    elif val > root.val:
        root.right = deleteRec(root.right, val)
    else:
        # One Child that is a leaf
        if root.left is None and root.right is not None:
            temp = root.right
            root.right = None
            return temp
        elif root.right is None and root.left is not None:
            temp = root.left
            root.left = None
            return temp

        # Two Children
        temp = findMinRec(root.right)
        root.val = temp.val
        root.right = deleteRec(root.right, temp.val)

    return root


def findNextRec(node):
    if node.right is not None:
        return findMinRec(node.right)
    else:
        return findNextParent(node, node.val)


def findNextParent(node, val):
    if node.parent is None:
        return None
    if node.parent.val > val:
        return node.parent
    else:
        return findNextParent(node.parent, val)


def findPrevRec(node):
    if node.left is not None:
        return findMaxRec(node.left)
    else:
        return findPrevParent(node, node.val)


def findPrevParent(node, val):
    if node.parent is None:
        return None
    if node.parent.val < val:
        return node.parent
    else:
        return findPrevParent(node.parent, val)


def findMinRec(node):
    if node.left is None:
        return node
    else:
        return findMinRec(node.left)


def findMaxRec(node):
    if node.right is None:
        return node
    else:
        return findMaxRec(node.right)


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


r = Node(10)
insertRec(r, Node(15))
insertRec(r, Node(2))
insertRec(r, Node(1))
insertRec(r, Node(8))
insertRec(r, Node(12))
insertRec(r, Node(20))
insertRec(r, Node(11))

print(findPrevRec(r.left.right).val)