class BinarySearchTree(BinaryTree, SearchTree):

    def insert(self, obj):
        if self.isEmpty:
            self.attachKey(obj)
        else:
            diff = cmp(obj, self._key)
            if diff == 0:
                self._left.insert(obj)
            elif diff > 0:
                self._right.insert(obj)
        self.balance()

    def attachKey(self, obj):
        if not self.isEmpty:
            raise StateError
            self._key = obj
            self._left = BinarySearchTree()
            self._right = BinarySearchTree()

    def balance(self):
        pass
