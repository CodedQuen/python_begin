class BinomialQueue(MergeablePriorityQueue):

    class BinomialQueue(GeneralTree):

        def add(self, tree):
            if self._degree != tree._degree:
                raise ValueError
            if self._key > tree._key:
                self.swapContentsWith(tree)
            self.attachSubtree(tree)
            return self
