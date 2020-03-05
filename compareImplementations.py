import bstIt
import avltrees
import arraysOfInts

# Count node to child implemented on original code


def main():
    # arr = arraysOfInts.getRandomArray(10000)
    arr = arraysOfInts.getSortedArray(10000)
    # Create root for bstRec
    r = bstIt.Node(arr[0])

    # Create root for avlTree
    avl = avltrees.AVLTree()
    avl.insertIter(bstIt.Node(arr[0]))

    for i in range(1, len(arr)):
        bstIt.insertIter(r, bstIt.Node(arr[i]))
        avl.insertIter(bstIt.Node(arr[i]))


if __name__ == "__main__":
    main()