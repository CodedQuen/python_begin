class GeneralTree(Tree):

    def __init__(self, key):
        super(GeneralTree, self).__init__()
        self._key = key
        self._degree = 0
        self._list = LinkedList()

    def purge(self):
        self._list.purge()
        self._degree = 0
