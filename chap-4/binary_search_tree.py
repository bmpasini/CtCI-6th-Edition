class TreeNode(object):

    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.val = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self ,key, value, lc, rc):
        self.key = key
        self.val = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self


class BinarySearchTree(object):

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self, key, val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size += 1

    def _put(self, key, val, x):
        if key < x.key:
            if x.hasLeftChild():
                self._put(key, val, x.leftChild)
            else:
                x.leftChild = TreeNode(key, val, parent=x)
        else:
            if x.hasRightChild():
                    self._put(key, val, x.rightChild)
            else:
                    x.rightChild = TreeNode(key, val, parent=x)

    def __setitem__(self, k, v):
       self.put(k, v)

    def get(self, key):
       if self.root:
            res = self._get(key, self.root)
            if res:
                return res.val
            else:
                return None
       else:
            return None

    def _get(self, key, x):
       if not x:
            return None
       elif x.key == key:
            return x
       elif key < x.key:
            return self._get(key, x.leftChild)
       else:
            return self._get(key, x.rightChild)

    def __getitem__(self, key):
       return self.get(key)

    def __contains__(self, key):
       if self._get(key, self.root):
           return True
       else:
           return False

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size-1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size-1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self,key):
       self.delete(key)

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                    self.leftChild.parent = self.parent
           else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                    self.rightChild.parent = self.parent

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def remove(self,x):
        if x.isLeaf(): #leaf
            if x == x.parent.leftChild:
                x.parent.leftChild = None
            else:
                x.parent.rightChild = None
        elif x.hasBothChildren(): #interior
            succ = x.findSuccessor()
            succ.spliceOut()
            x.key = succ.key
            x.val = succ.val

        else: # this node has one child
            if x.hasLeftChild():
                if x.isLeftChild():
                    x.leftChild.parent = x.parent
                    x.parent.leftChild = x.leftChild
                elif x.isRightChild():
                    x.leftChild.parent = x.parent
                    x.parent.rightChild = x.leftChild
                else:
                    x.replaceNodeData(x.leftChild.key,
                                      x.leftChild.val,
                                      x.leftChild.leftChild,
                                      x.leftChild.rightChild)
            else:
                if x.isLeftChild():
                    x.rightChild.parent = x.parent
                    x.parent.leftChild = x.rightChild
                elif x.isRightChild():
                    x.rightChild.parent = x.parent
                    x.parent.rightChild = x.rightChild
                else:
                    x.replaceNodeData(x.rightChild.key,
                                      x.rightChild.val,
                                      x.rightChild.leftChild,
                                      x.rightChild.rightChild)


if __name__ == "__main__":
    mytree = BinarySearchTree()
    mytree[3]="red"
    mytree[4]="blue"
    mytree[6]="yellow"
    mytree[2]="at"
    print(mytree[6])
    print(mytree[2])
