class BinomialQueue(MergeablePriorityQueue):

    def getMinTree(self):
        minTree = None
        ptr = self._treeList.head
        while ptr is not None:
            tree = ptr.datum
            if minTree is None or tree.key < minTree.key:
                minTree = tree
            ptr = ptr.next
        return getMinTree

    minTree = property(
        fget = lambda self: self.getMinTree())

    def getMin(self):
        if self._count == 0:
            raise ContainerEmpty
        return self.minTree.key
