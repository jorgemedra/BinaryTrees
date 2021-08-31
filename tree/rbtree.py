
from btree import BNode
from btree import BTree

'''
Use http://gregfjohnson.com/cgi-bin/redblackbuilder to validate the outcome tree
'''


class RBNode(BNode):
    
    def __init__(self,  key, value, Nil):
        super().__init__(key, value)
        self.color = True #By default, its color is RED
        self.parent = Nil
        self.left = Nil
        self.right = Nil

class RBTree(BTree):

    RED = True
    BLACK = False

    def __init__(self):
        nil = RBNode(None, None, None)
        super().__init__(nil)
        # Create a Node wich replaces NONE to work as a Nil,
        # which will be used as a Node to valid its color (BLACK)        
        self.Nil.color = self.BLACK #Nil node will be BLACK
        self.Nil.key = None
        self.Nil.value = None
        self.Nil.parent = self.Nil
        self.Nil.left = self.Nil
        self.Nil.right = self.Nil
        self.root = self.Nil

    def InsertByKV(self, key, value):
        x = RBNode(key,value, self.Nil)
        self.Insert(x)
        return x

    def Insert(self, z:RBNode):
        super().Insert(z)
        self.FixInsertion(z)
        
    def IsUncleRed(self, x):
        kindchild = self.KindOfChild(x.parent)
        if kindchild < 0:  # Parent is the Left Child
            return True if x.parent.parent.right.color == self.RED else False
        
        return True if x.parent.parent.left.color == self.RED else False

    def SetUnclesColor(self, color, x):
        kindchild = self.KindOfChild(x.parent)
        if kindchild < 0: # Parent is the Left Child
            x.parent.parent.right.color = color
        else:
            x.parent.parent.left.color = color

    def FixInsertion(self, z: RBNode):
        '''
        Source https://www.amazon.com/Introduction-Algorithms-3rd-MIT-Press/dp/0262033844
        Note: I Made some changes to the Algorith described on page 316, because i found
        out some mistakes, according with my implementation.
        '''

        while z.parent.color == self.RED:
            kindchild = self.KindOfChild(z.parent)

            if kindchild < 0: # Is the left child

                y = z.parent.parent.right

                #Case 1
                if y.color == self.RED:
                    z.parent.color = self.BLACK
                    y.color = self.BLACK
                    z.parent.parent.color = self.RED
                    z = z.parent.parent
                
                else:
                    kindchild = self.KindOfChild(z)
                    #Case 2
                    if kindchild > 0:  # Right Child
                        self.RotLeft(z)    
                        z = z.left
                    
                    #Case 3                    
                    z.parent.color = self.BLACK
                    if z.parent.parent != self.Nil:
                        z.parent.parent.color = self.RED
                    self.RotRight(z.parent)

            else:  # IS the right child
                y = z.parent.parent.left

                #Case 1
                if y.color == self.RED:
                    z.parent.color = self.BLACK
                    y.color = self.BLACK
                    z.parent.parent.color = self.RED
                    z = z.parent.parent

                else:
                    kindchild = self.KindOfChild(z)
                    #Case 2
                    if kindchild < 0:  # Left Child
                        self.RotRight(z)
                        z = z.right

                    #Case 3                    
                    z.parent.color = self.BLACK     
                    if z.parent.parent != self.Nil:
                        z.parent.parent.color = self.RED
                    self.RotLeft(z.parent)
            
        self.root.color = self.BLACK        
        #return z
   
    def RBTransplant(self, y, x):
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
        y.parent = x.parent

    def Delete(self, z):
        '''
        Source https://www.amazon.com/Introduction-Algorithms-3rd-MIT-Press/dp/0262033844
        Note: I tried to implement the algorithm of page 326, but it has some incosistence, accorfing with me,
        so i decide to implement the cases which are described on pages 327 and 328.
        '''

        if z == self.Nil:
            return self.Nil  # For future implementation, inherencies.

        y = z
        ocolor = z.color        
        self.FixMinMaxDel(z)
        
        if z.left == self.Nil:  # Just Right child
            x = z.right
            self.RBTransplant(z.right, z)
        elif z.right == self.Nil:   # Just left child
            x = z.left
            self.RBTransplant(z.left, z)
        else:  # has both children
            y = self.Min(z.right) #Get the successor                   
            ocolor = y.color
            x = y.right            
            self.FixMinMaxDel(y)

            if y.parent == z: 
                x.parent = y
            else:
                self.RBTransplant(y.right, y)
                y.right = z.right
                y.right.parent = y
            
            self.RBTransplant(y, z)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if ocolor == self.BLACK:
            self.Fix_Delete(x)
        
        self.count -= 1

    def Fix_Delete(self, x):
        
        while x != self.root and x.color == self.BLACK:
            if x.parent.left == x:  # Left child
                w = x.parent.right

                if w.color == self.RED: #Case 1, Sibiling is RED
                    w.color = self.BLACK
                    x.parent.color = self.RED
                    self.RotLeft(x.parent)
                else: #Sibiling is BLACK
                    #w.left.color == self.BLACK and
                    
                    #Case 2, Sibiling is Black and both of its children are Black
                    if w.right.color == self.BLACK and w.left.color == self.BLACK:
                        w.color = self.RED
                        x = x.parent
                    else:
                        # Case 3
                        if w.left.color == self.RED and w.right.color == self.BLACK:
                            w.left.color = self.BLACK
                            w.color = self.RED
                            self.RotRight(w.left)
                            w = w.parent 
                        
                        #Case 4
                        w.color = x.parent.color
                        x.parent.color = self.BLACK
                        w.right.color = self.BLACK
                        self.RotLeft(w)
                        x = self.root

            else:   #Right child
                w = x.parent.left

                if w.color == self.RED:  # Case 1, Sibiling is RED
                    w.color = self.BLACK
                    x.parent.color = self.RED
                    self.RotRight(x.parent)
                else:  # Sibiling is BLACK
                    #w.right.color == self.BLACK and

                    #Case 2, Sibiling is Black and both of its children are Black
                    if w.right.color == self.BLACK and w.left.color == self.BLACK:
                        w.color = self.RED
                        x = x.parent
                    else:
                        # Case 3
                        if w.right.color == self.RED and w.left.color == self.BLACK:
                            w.right.color = self.BLACK
                            w.color = self.RED
                            self.RotLeft(w.right)
                            w = w.parent  

                        #Case 4
                        w.color = x.parent.color
                        x.parent.color = self.BLACK
                        w.left.color = self.BLACK
                        self.RotRight(w)
                        x = self.root

        x.color = self.BLACK
                

            
            
