class Node:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class AVLTree(object):

    def __init__(self):
        self.root = None

    def insertIter(self, n: Node):
        if self.root is None:
            self.root = n
            return

        count = 0
        curr = self.root
        parent = None
        while curr is not None:
            parent = curr
            if n.val > curr.val:
                curr = curr.right
            else:
                curr = curr.left
            count += 1

        if n.val > parent.val:
            parent.right = n
            parent.right.parent = parent
        else:
            parent.left = n
            parent.left.parent = parent

        curr = parent
        while curr is not None:
            # Two Children
            if curr.left is not None and curr.right is not None:
                if self.BF(curr) > 1 and (self.BF(curr.left) > 0 or self.BF(curr.right) > 0):
                    self.rightRot(curr)
                elif self.BF(curr) < -1 and (self.BF(curr.left) < 0 or self.BF(curr.right) < 0):
                    self.leftRot(curr)
                elif self.BF(curr) < -1 and self.BF(curr.left) > 0:
                    self.rightRot(curr.left)
                    self.leftRot(curr)
                elif self.BF(curr) < -1 and self.BF(curr.right) > 0:
                    self.rightRot(curr.right)
                    self.leftRot(curr)
                elif self.BF(curr) > 1 and self.BF(curr.left) < 0:
                    self.leftRot(curr.left)
                    self.rightRot(curr)
                elif self.BF(curr) > 1 and self.BF(curr.right) < 0:
                    self.leftRot(curr.right)
                    self.rightRot(curr)
            # Left Child only
            elif curr.left is not None and curr.right is None:
                if self.BF(curr) > 1 and self.BF(curr.left) >= 0:
                    self.rightRot(curr)
                elif self.BF(curr) < -1 and self.BF(curr.left) <= 0:
                    self.leftRot(curr)
                elif self.BF(curr) > 1 and self.BF(curr.left) < 0:
                    self.leftRot(curr.left)
                    self.rightRot(curr)
                elif self.BF(curr) < -1 and self.BF(curr.left) > 0:
                    self.rightRot(curr.left)
                    self.rightRot(curr)
            # Right Child only
            elif curr.left is None and curr.right is not None:
                if self.BF(curr) > 1 and self.BF(curr.right) >= 0:
                    self.rightRot(curr)
                elif self.BF(curr) < -1 and self.BF(curr.right) <= 0:
                    self.leftRot(curr)
                elif self.BF(curr) > 1 and self.BF(curr.right) < 0:
                    self.leftRot(curr.right)
                    self.rightRot(curr)
                elif self.BF(curr) < -1 and self.BF(curr.right) > 0:
                    self.rightRot(curr.right)
                    self.leftRot(curr)

            curr = curr.parent
        print("avltree: " + str(count))

    def deleteIter(self, val: int):
        curr = self.root

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
            nextNode = self.findNextIter(curr)

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

        # Balance Tree

        while curr is not None:
            # Two Children
            if curr.left is not None and curr.right is not None:
                if self.BF(curr) > 1 and (self.BF(curr.left) > 0 or self.BF(curr.right) > 0):
                    self.rightRot(curr)
                elif self.BF(curr) < -1 and (self.BF(curr.left) < 0 or self.BF(curr.right) < 0):
                    self.leftRot(curr)
                elif self.BF(curr) < -1 and self.BF(curr.left) > 0:
                    self.rightRot(curr.left)
                    self.leftRot(curr)
                elif self.BF(curr) < -1 and self.BF(curr.right) > 0:
                    self.rightRot(curr.right)
                    self.leftRot(curr)
                elif self.BF(curr) > 1 and self.BF(curr.left) < 0:
                    self.leftRot(curr.left)
                    self.rightRot(curr)
                elif self.BF(curr) > 1 and self.BF(curr.right) < 0:
                    self.leftRot(curr.right)
                    self.rightRot(curr)
            # Left Child only
            elif curr.left is not None and curr.right is None:
                if self.BF(curr) > 1 and self.BF(curr.left) >= 0:
                    self.rightRot(curr)
                elif self.BF(curr) < -1 and self.BF(curr.left) <= 0:
                    self.leftRot(curr)
                elif self.BF(curr) > 1 and self.BF(curr.left) < 0:
                    self.leftRot(curr.left)
                    self.rightRot(curr)
                elif self.BF(curr) < -1 and self.BF(curr.left) > 0:
                    self.rightRot(curr.left)
                    self.rightRot(curr)
            # Right Child only
            elif curr.left is None and curr.right is not None:
                if self.BF(curr) > 1 and self.BF(curr.right) >= 0:
                    self.rightRot(curr)
                elif self.BF(curr) < -1 and self.BF(curr.right) <= 0:
                    self.leftRot(curr)
                elif self.BF(curr) > 1 and self.BF(curr.right) < 0:
                    self.leftRot(curr.right)
                    self.rightRot(curr)
                elif self.BF(curr) < -1 and self.BF(curr.right) > 0:
                    self.rightRot(curr.right)
                    self.leftRot(curr)

            curr = curr.parent

    def findNextIter(self, n: Node):
        if n.right is not None:
            return self.findMinIter(n.right)

        curr = n
        while curr.parent.val < n.val:
            curr = curr.parent
            if curr.parent is None:
                return None
        return curr.parent

    def findPrevIter(self, n: Node):
        if n.left is not None:
            return self.findMaxIter(n.left)

        curr = n
        while curr.parent.val > n.val:
            curr = curr.parent
            if curr.parent is None:
                return None
        return curr.parent

    def findMinIter(self, n: Node):
        curr = n
        while curr.left is not None:
            curr = curr.left
        return curr

    def findMaxIter(self, n: Node):
        curr = n
        while curr.right is not None:
            curr = curr.right
        return curr

    def rightRot(self, n: Node):
        rot = n.left
        temp = rot.right

        if n == self.root:
            rot.parent = None
            self.root = rot
        elif rot.val > n.parent.val:
            rot.parent = n.parent
            n.parent.right = rot
        else:
            rot.parent = n.parent
            n.parent.left = rot

        rot.right = n
        rot.right.parent = rot
        n.left = temp
        if temp is not None:
            temp.parent = n

    def leftRot(self, n: Node):
        rot = n.right
        temp = rot.left

        if n == self.root:
            rot.parent = None
            self.root = rot
        elif rot.val < n.parent.val:
            rot.parent = n.parent
            n.parent.left = rot
        else:
            rot.parent = n.parent
            n.parent.right = rot

        rot.left = n
        rot.left.parent = rot
        n.right = temp
        if temp is not None:
            temp.parent = n

    def BF(self, n: Node):
        return self.getHeight(n.left) - self.getHeight(n.right)

    def getHeight(self, n: Node):
        if n is None:
            return 0
        else:
            l = self.getHeight(n.left)
            r = self.getHeight(n.right)

            if l > r:
                return l + 1
            else:
                return r + 1

    def inorder(self, root: Node):
        if root is not None:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)


COUNT = [10]


def print2DUtil(root, space):
    # Base case
    if root is None:
        return

    # Increase distance between levels
    space += COUNT[0]

    # Process right child first
    print2DUtil(root.right, space)

    # Print current node after space
    # count
    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print(root.val)

    # Process left child
    print2DUtil(root.left, space)


# Wrapper over print2DUtil()
def print2D(root):
    # space=[0]
    # Pass initial space count as 0
    print2DUtil(root, 0)


def main():
    test = AVLTree()
    test.insertIter(Node(18))
    test.insertIter(Node(22))
    test.insertIter(Node(67))
    test.insertIter(Node(38))
    test.insertIter(Node(65))
    test.insertIter(Node(60))
    test.insertIter(Node(71))
    test.insertIter(Node(99))
    test.insertIter(Node(93))
    test.insertIter(Node(94))
    test.insertIter(Node(85))


if __name__ == "__main__":
    main()