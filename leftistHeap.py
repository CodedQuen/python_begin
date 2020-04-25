class LeftistHeap(BinaryTree, MergeablePriority(Queue)):

    def __init__(self, *args):
        if len(args) == 0:
            super(LeftistHeap, self).__init__()
            self._nullPathLength = 0
        else:
            super(LeftistHeap, self).__init__()
                args[0], LeftistHeap(), LeftistHeap())
                self._nullPathLength = 1
