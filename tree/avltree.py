
#from avl.btree import BNode
#from avl.btree import BTree

from btree import BNode
from btree import BTree

class AVLNode(BNode):
    
    def __init__(self, key, value):
        super().__init__(key, value)
        self.heigh = 0


class AVLTree (BTree):

    def __init__(self):
        super().__init__()

    def Maxheigh(self, x: AVLNode):
        if x != None:
            children = self.HasChildren(x)
            if children == 2: # Both Children
                return x.left.heigh if x.left.heigh > x.right.heigh else x.right.heigh
            elif children < 0: # Just Left children
                return x.left.heigh  
            elif children > 0:  # Just Right children
                return x.right.heigh
        return 0

    def CalculateMaxheight(self, x):
        x.heigh = 1 + self.Maxheigh(x)

    def RotLeft(self, y):
        super().RotLeft(y)
        self.CalculateMaxheight(y.left)
        self.CalculateMaxheight(y)        

    def RotRight(self, y):
        super().RotRight(y)
        self.CalculateMaxheight(y.right)
        self.CalculateMaxheight(y)
    
    def InsertByKV(self, key, value):
        x = AVLNode(key, value)
        self.Insert(x)

    def Insert(self, x: AVLNode):  
        super().Insert(x)
        self.BalanceNode(x)
        return x
        
    def BalanceFactor(self, x:AVLNode):
        if x == None:
            return 0

        lh = x.left.heigh if x.left != None else 0
        rh = x.right.heigh if x.right != None else 0
        return lh - rh
        
    def BalanceNode(self, x: AVLNode):
        y: AVLNode = x

        while x != self.Nil:
            self.CalculateMaxheight(x)
            fact = self.BalanceFactor(x)
            
            if abs(fact) > 1:
                if fact > 1:                        # Heaviest on Left
                    cFact = self.BalanceFactor(x.left)
                    if cFact < 0:   # CASE 1'                        
                        self.RotLeft(x.left.right)
                    self.RotRight(x.left)       # CASE 2'                    
                else:                      # Heaviest on Right
                    cFact = self.BalanceFactor(x.right)
                    if cFact > 0:                   # CASE 1'
                        self.RotRight(x.right.left)                    
                    self.RotLeft(x.right)       # CASE 2'                    

            if x.parent == self.Nil:
                self.root = x
            x = x.parent
            
        #return y

    def Delete(self, x:AVLNode):
        p = super().Delete(x)
        self.BalanceNode(p)

def Test1():    
    #numbers = (10, 9, 8)
    #numbers = (10, 8, 9)
    #numbers = (14, 17, 11, 7, 53, 4)
    #numbers = (14, 17, 11, 7, 53, 9)
    #numbers = (14, 17, 11, 7, 53, 4, 13, 12, 8, 60, 19, 16, 20, 18)
    #numbers = (14, 17, 11, 7, 53, 4, 13, 12, 8, 60, 19, 16, 20, 18)
    numbers = (40,30,50,20,10,60,70,80,45,55)
    
    T = AVLTree()

    for x in numbers:
        T.InsertByKV(x,x)

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

def Test2():
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

if __name__ == '__main__':
    Test1()
    Test2()
