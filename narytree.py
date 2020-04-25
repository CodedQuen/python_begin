class NaryTree(Tree):

    def __init__(self, *args):
        super(NaryTree, self).__init__()
        if len(args) == 1:
            self._degree = args[0]
            self._key = None
            self._subtree = None
        elif len(args) == 2:
            self._degree = args[0]
            self._key = args[1]
            self._subtree = Array(self._degree)
            for i in range(self._degree):
                self._subtree[i] = NaryTree(self._degree)

    def purge(self):
        self._key = None
        self._subtree = None
