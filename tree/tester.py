
from btree import BTree
from btree import BNode
from avltree import AVLNode
from avltree import AVLNode
from rbtree import RBTree
from rbtree import RBNode


'''
------------------------------------------------------------------------
Binary Tree Test
------------------------------------------------------------------------
'''

def BTreeTest():
    BTest1()
    BTest2()
    BTest3()
    
def BTest1():
    print('''
..............................................
Testing 1 Insert, print InOrder, PostOrder 
and PreOrder
..............................................
    ''')

    #numbers = (14, 17, 11, 7, 53, 4)
    numbers = (30, 40, 20, 25, 10, 35, 50, 5, 15, 7, 9, 35, 60, 55)

    T = BTree()
    for x in numbers:
        n = BNode(x, x)
        T.Insert(n)

    print("\nPrinting ASC:\n")
    n = T.Begin()
    while n != None:
        print("[{}:{}]".format(n.key, n.value), end=" ")
        n = T.Next(n)
    print("\n------------\n")

    print("\nPrinting DESC:\n")
    n = T.End()
    while n != None:
        print("[{}:{}]".format(n.key, n.value), end=" ")
        n = T.Prev(n)

    print("\n------------\n")

    print("\nPrinting Pre Order:\n")
    T.PrintPreOrder(T.root)
    print("\n------------\n")

    print("\nPrinting In Order:\n")
    T.PrintInOrder(T.root)
    print("\n------------\n")

    print("\nPrinting Post Order:\n")
    T.PrintPostOrder(T.root)
    print("\n------------\n")


def BTest2():
    print('''
..............................................
Testing 2 Rotating Left and Right.
..............................................
    ''')

    #numbers = ((10,'y'), (5,'x'), (15,'a'), (4,'b'), (6,'c'), (14,'d'), (16,'e'))
    numbers = ((10, 'y'), (9, 'x'), (7, 'a'),
               (8, 'b'), (5, 'c'), (3, 'd'), (4, 'e'))

    T = BTree()
    for x in numbers:
        n = BNode(x[0], x[1])
        T.Insert(n)

    print("\nBefore Rot Right (Pre Order):\n")
    T.PrintPreOrder(T.root)
    print("\n------------\n")

    x = T.findNode(8)
    T.RotLeft(x)
    print("\nAfter Rot Right (Pre Order):\n")
    T.PrintPreOrder(T.root)
    print("\n------------\n")

    x = T.findNode(5)
    T.RotRight(x)
    print("\nAfter Rot Right (Pre Order):\n")
    T.PrintPreOrder(T.root)
    print("\n------------\n")

    x = T.findNode(10)
    T.RotLeft(x)
    print("\nAfter Rot left (Pre Order):\n")
    T.PrintPreOrder(T.root)
    print("\n------------\n")


def BTest3():
    print('''
..............................................
Testing 3 Deleting
..............................................
    ''')

    numbers = (50, 40, 30, 45, 10, 35, 60, 55, 80, 70, 90)
    DeletOrder = (10, 35, 40, 60, 70, 50, 30, 90, 55, 45, 80,)

    T = BTree()
    for x in numbers:
        n = BNode(x, x)
        T.Insert(n)

    print("\nOriginal):\n")
    T.PrintPreOrder(T.root)
    print("\nMIN: {0}; Max: {1}".format(T.Begin().key, T.End().key))
    print("\n------------\n")

    for x in DeletOrder:
        print("\nDeleting {0}:\n".format(x))
        n = T.findNode(x)
        T.Delete(n)
        T.PrintPreOrder(T.root)
        if T.count > 0:
            print("\nMIN: {0}; Max: {1}".format(T.Begin().key, T.End().key))
        else:
            print("\nNo more elements into the three.")
        print("\n------------\n")


'''
------------------------------------------------------------------------
AVL Tree Test
------------------------------------------------------------------------
'''

def AVLTreeTest():
    AVLTest1()
    AVLTest2()

def AVLTest1():
    #numbers = (10, 9, 8)
    #numbers = (10, 8, 9)
    #numbers = (14, 17, 11, 7, 53, 4)
    #numbers = (14, 17, 11, 7, 53, 9)
    #numbers = (14, 17, 11, 7, 53, 4, 13, 12, 8, 60, 19, 16, 20, 18)
    #numbers = (14, 17, 11, 7, 53, 4, 13, 12, 8, 60, 19, 16, 20, 18)
    numbers = (40, 30, 50, 20, 10, 60, 70, 80, 45, 55)

    T = AVLTree()

    for x in numbers:
        T.InsertByKV(x, x)

    print("------ IN ORDER ---- ")
    T.PrintInOrder(T.root)
    print(".")
    print("\n------------\n")

    print("\nPrinting ASC:\n")
    n = T.Begin()
    while n != None:
        print("[{}:{}]".format(n.key, n.value), end=" ")
        n = T.Next(n)
    print(".")
    print("\n------------\n")

    print("\nPrinting DESC:\n")
    n = T.End()
    while n != None:
        print("[{}:{}]".format(n.key, n.value), end=" ")
        n = T.Prev(n)
    print(".")
    print("\n------------\n")

def AVLTest2():
    #Case 1
    #numbers = (1,2,3,4,5)
    # Case 2

    #numbers = (14, 17, 11, 7, 53, 4)
    #numbers = (14, 17, 11, 7, 53, 9)
    numbers = (14, 17, 11, 7, 53, 4, 13, 12, 8, 60, 19, 16, 20, 18)
    #numbers = (14, 17, 11, 7, 53, 4, 13, 12, 8, 60, 19, 16, 20, 18)

    T = AVLTree()

    for x in numbers:
        T.InsertByKV(x, x)

    print("------ IN ORDER ---- ")
    T.PrintInOrder(T.root)
    print(".")

    numbers = (16, 14)
    for x in numbers:
        print("------ Deleting {0}---- ".format(x))
        n = T.findNode(x)
        T.Delete(n)
        T.PrintInOrder(T.root)
        print(".")

    print("\nPrinting ASC:\n")
    n = T.Begin()
    while n != None:
        print("[{}:{}]".format(n.key, n.value), end=" ")
        n = T.Next(n)
    print(".")


'''
------------------------------------------------------------------------
RB Tree Test
------------------------------------------------------------------------
'''

def RBTreeTest():
    RBTTest1()
    RBTTest2()

def RBTTest1():
    
    #numbers = (50, 40, 30, 45, 10, 35, 60, 55, 80, 70, 90)
    #numbers = (40, 30, 50,20,10)
    #numbers = (40, 30, 50, 20, 10, 60, 70)
    #numbers = (40, 30, 50, 20, 10, 60, 70, 80)
    #numbers = (40, 30, 50, 20, 10, 60, 70, 80, 45,55)
    numbers = (40, 30, 50, 20, 10, 60, 70, 80, 45, 55, 53)

    T = RBTree()
    for x in numbers:
        n = RBNode(x, x, T.Nil)
        T.Insert(n)
        
    T.PrintInOrder(T.root)
    print("\n------------\n")

def RBTTest2():

    '''
    Original Tree:
                                50 (b)
                40 (r)                          60 (r)
        20 (b)          45 (b)          55(b)           70(b)
    10(r)   30(r)                   53(r)                   80(r)


    Deleting Sequence: 50,55,45,10, 30, 40, 53, 20, 70

    Final Tree:

            80 (b)
        60 (r)

    '''

    numbers = (40, 30, 50, 20, 10, 60, 70, 80, 45, 55, 53)

    delNumbers = (50,55,45,10, 30, 40, 53, 20, 70)

    T = RBTree()
    for x in numbers:
        n = RBNode(x, x, T.Nil)
        T.Insert(n)
    
    T.PrintInOrder(T.root)
    print("\n------------\n")

    for x in delNumbers:
        print("Deleting {0}\n".format(x))
        n = T.findNode(x)  # OK        
        T.Delete(n)
    
    print("\n------------\n")
    T.PrintInOrder(T.root)


if __name__ == "__main__":
    
    BTreeTest();
    AVLTreeTest;
    RBTreeTest()
