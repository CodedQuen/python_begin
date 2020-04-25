class BinarySearchTree(BinaryTree, SearchTree):

    def find(self, obj):
        if self.isEmpty:
            return None
        diff = cmp(obj, self._key)
        if diff == 0:
            return self._key
        elif diff < 0:
            return self._left.find(obj)
        elif diff > 0:
            return self._right.find(obj)

    def getMin(self):
        if self.isEmpty:
            return None
        elif self._left.isEmpty:
            return self._key
        else:
            return self._left.min
