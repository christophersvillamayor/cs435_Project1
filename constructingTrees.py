import bstRec
import bstIt
import avltrees
import arraysOfInts


def main():
    # arr = arraysOfInts.getRandomArray(10000)
    arr = arraysOfInts.getRandomArray(10)

    # Create root for bstRec
    r = bstRec.Node(arr[0])

    # Create root for avlTree
    avl = avltrees.AVLTree()
    avl.insertIter(bstRec.Node(arr[0]))

    for i in range(1, len(arr)):
        #bstRec.insertRec(r, bstRec.Node(arr[i]))
        bstIt.insertIter(r, bstRec.Node(arr[i]))
        avl.insertIter(bstRec.Node(arr[i]))

if __name__ == "__main__":
    main()
