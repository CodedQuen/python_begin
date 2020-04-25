class BinomialQueue(MergeablPriorityQueue):

    def __init__(self, *args):
        super(BinomialQueue, self).__init__()
        self._treeList = LinkedList()
        if len(args) == 0:
            pass
        elif len(args) == 1:
            assert isinstance(args[0], self.BinomialQueue)
            self._treeList.append(args[0])
        else:
            raise ValueError
