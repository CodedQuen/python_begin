class AVLTree(BinarySearchTree):

    def getHeight(self):
        return self._height

    def adjustHeight(self):
        if self.isEmpty:
            self._height = -1

        else:
            self._height = 1 + max (self._left._height, self._right._height)

    def getBalanceFactor(self):
        if self.isEmpty:
            return 0
        else:
            return self._left._height - self._right._height

    getBalanceFactor = property(
            fget = lambda self: self.getBalanceFactor())
