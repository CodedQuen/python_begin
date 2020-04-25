class BTree(MWayTree):

    def __init__(self, m):
        super(BTree, self).__init__(m)

    def attachSubtree(self, i, t):
        self._subtree[i] = t
        t._parent = self
