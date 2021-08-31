
class BNode:
    
    def __init__(self, key, value):
        #self.Nil = None
        self.parent = None
        self.left = None
        self.right = None
        self.key = key
        self.value = value
        
class Comparator:    
    def __init__(self):
        pass

    def LT(self, x: BNode, y: BNode):
        return x.key < y.key
    
    #def EQ(self, x: BNode, y: BNode):
    #    return not self.LT(x, y) and not self.LT(y, x)

class BTree:

    def __init__(self, Nil=None, cmp=Comparator()):
        self.Nil = Nil  # For future implementation on RBTrees
        self.root = Nil
        self.count = 0
        self.cmp = cmp
        self.__min = Nil
        self.__max = Nil
    
    '''
    Adding, Deleting and transplanting
    '''

    def InsertByKV(self, key, value):
        x = BNode(key,value)
        self.Insert(x)
        return x

    def Insert(self, node):
        '''
        O(long n)
        Add a Key:Value BNode to the tree and at the same time it will update the max or min pointer.
        '''
        if node == self.Nil:
            return


        if self.root != self.Nil:
            
            naux = self.root
        
            while True:
                nnode = naux.left if self.cmp.LT(node, naux) else naux.right

                if nnode == self.Nil:
                    break
                else:
                    naux = nnode

            if self.cmp.LT(node, naux): 
                naux.left = node
                if naux == self.__min:  # update minimun or maximum pointer
                    self.__min = node
            else:
                naux.right = node
                if naux == self.__max:  # update minimun or maximum pointer
                    self.__max = node
            
            node.parent = naux

        else:
            self.root = node
            self.__min = node
            self.__max = node

        self.count = self.count +1
    
    def Transplant(self, y, x):
        '''
        This function will replace the node X by the node Y
        changin only the parents, and leaving the child modification
        to the function caller.
        '''
        
        kchild = self.KindOfChild(x) 
        if x.parent == self.Nil:  # X is the root
            self.root = y
        #elif x.parent.left == x: # X is the left child
        elif kchild == -1: # X is the left child
            x.parent.left = y
        elif kchild == 1: # X is the right child
            x.parent.right = y

        if y != self.Nil:
            y.parent = x.parent
        
    def FixMinMaxDel(self, x, y):
        
        if y == self.Nil:
            if x == self.__min:
                self.__min = x.parent
            if x == self.__max:
                self.__max = x.parent
        else:
            if x == self.__min:
                self.__min = y
            if x == self.__max:
                self.__max = y

    def Delete(self, x):
        '''
        Delete a node from the three.

        Return the node's parent from where it was taken. 
        It will be used to implement the AVLTree and RBTree.

        '''
        if x == self.Nil:
            return self.Nil # For future implementation, inherencies.

        y = self.Nil
        p = x.parent

        #self.FixMinMaxDel(x)

        children = self.HasChildren(x)
        # Case 1, the node doesn't have children.
        if children == 0:
            y = self.Nil 
            self.FixMinMaxDel(x, y)
        elif children != 2: # has one child, which take it's place        
            y = x.right if children > 0 else x.left
            self.FixMinMaxDel(x, y)
        else: # It has both children
            y = self.Min(x.right)
            p = y.parent            
            self.FixMinMaxDel(x, y)

            self.Transplant(y.right, y)
            y.parent = self.Nil

        self.Transplant(y,x) # Only modify parents.

        if y != self.Nil:
            y.left = x.left 
            y.right = x.right

            if y.left != self.Nil:
                y.left.parent = y
            if y.right != self.Nil:
                y.right.parent = y
            
        if x == self.root:
            self.root = y
        
        self.count -= 1
        return p

    def RotRight(self, y):
        '''
        Rotate the node to Right

        ''' 

        if y == self.root:
            return

        x = y.parent
        xc = self.KindOfChild(x) 
        xp = x.parent

        y.parent = x.parent
        x.left = y.right
        y.right = x
        x.parent = y

        if x.left != self.Nil:
            x.left.parent = x

        if xc == 0:
            self.root = y
        elif xc < 1:
            xp.left = y
        else:
            xp.right = y
      
    def RotLeft(self, y):
        '''
        Rotate the node to Left         
        '''

        if y == self.root:
            return

        x = y.parent
        xc = self.KindOfChild(x)
        xp = x.parent
        
        y.parent = x.parent
        x.right = y.left
        y.left = x
        x.parent = y

        if x.right != self.Nil:
            x.right.parent = x

        if xc == 0:
            self.root = y
        elif xc < 1:
            xp.left = y
        else:
            xp.right = y
        

    '''
    Finding
    '''

    def Min(self, node=None):
        '''
        O(log n)
        Get the minimum value in the tree
        '''
        if node == self.Nil:
            node = self.root

        x = node.left
        while x != self.Nil:
            node = x
            x = node.left
        return node
        
    def Max(self, node=None):
        '''
        O(1)
        Get the maximum value in the tree
        '''
        if node == self.Nil:
            node = self.root

        x = node.right
        while x != self.Nil:
            node = x
            x = node.right
        return node
    
    def findNode(self, key):
        '''
        O(long n)
        Search a node wich Key is equal to a specific value.
        '''
        naux = BNode(key, None)

        node = self.root
        while node != self.Nil:
            if not self.cmp.LT(node, naux) and not self.cmp.LT(naux, node):
                break
            else:
                node = node.left if self.cmp.LT(naux, node) else node.right

        return node

    '''
    Basic Queries
    '''

    def HasChildren(self, x):
        '''
        0 = has no Children
        -1 = Just has left child
        1 = just has right Child
        2 = has both chilren
        '''
        if x.left != self.Nil and x.right != self.Nil:
            return 2
        elif x.left == self.Nil and x.right != self.Nil:
            return 1
        elif x.left != self.Nil and x.right == self.Nil:
            return -1

        return 0

    def KindOfChild(self, x):
        '''
        0 = Has no parent or NIL
        -1 =It's left Child
        1 = It's right child
        '''

        if x.parent == self.Nil:
            return 0
        elif x.parent.left == x:
            return -1

        return 1
        

    '''
    Navigating
    '''    

    def Begin(self):
        '''
        O(1)
        The first node is the minumun Key of the tree. It will take the pointer to self.__min
        '''
        return self.__min #self.Min(self.root)
    
    def End(self):
        '''
        O(1)
        The last node is the maximum Key of the tree. It will take the pointer to self.__max
        '''
        return self.__max # self.Max(self.root)

    def Next(self,node):
        if node == self.Nil:
            return self.Nil

        if node.right != self.Nil:  # Case 1
            return self.Min(node.right)
        else:
            # Case 2
            if node == node.parent.left:
                return node.parent
            else:  # Case 3
                x = node
                while x != self.root and x == x.parent.right:
                    x = x.parent
                if x != self.root:
                    return x.parent

        return self.Nil

    def Prev(self,node):
    
        if node == self.Nil:
            return self.Nil
    
        if node.left != self.Nil:  # Case 1: it has the left child or it is the Root.
            return self.Max(node.left)
        else:
            # Case 2
            if node == node.parent.right:
                return node.parent
            else: # Case 3
                x = node
                while x != self.root and x == x.parent.left:
                    x = x.parent        
                if x != self.root:
                    return x.parent

        return self.Nil


    '''
    Printing
    '''

    def PrintPreOrder(self, node = None):
        if node != self.Nil:
            print("[{}:{}]".format(node.key, node.value), end=" ")
            self.PrintPreOrder(node.left)
            self.PrintPreOrder(node.right)

    def PrintInOrder(self, node = None):
        if node != self.Nil:
            self.PrintInOrder(node.left)
            print("[{}:{}]".format(node.key, node.value), end=" ")
            self.PrintInOrder(node.right)
    
    def PrintPostOrder(self, node = None):
        if node != self.Nil:
            self.PrintPostOrder(node.left)
            self.PrintPostOrder(node.right)
            print("[{}:{}]".format(node.key, node.value), end=" ")

