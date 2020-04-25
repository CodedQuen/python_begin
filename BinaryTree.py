class BinaryTree(Tree):

    def __init__(self, *args):
        super(BinaryTree, self).__init__()
        if len(args) == 0:
            self._key = None
            self._left = None
            self._right = None
        elif len(args) == 1:
            self._key = args[0]
            self._left = BinaryTree()
            self._right = BinaryTree()
        elif len(args) == 3:
            self._key = args[0]
            self._left = args[1]
            self._right = args[2]
        else:
            raise ValueError

    def purge(self):
            self._key = None
            self._left = None
            self._right = None
