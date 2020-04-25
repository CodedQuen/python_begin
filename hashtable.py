class HashTable(SearchableContainer):

    def __init__(self):
        super(HashTable, self).__init__()

    def __len__(self):
        pass

    __len__ = abstractmethod(__len__)

    def getLoadFactor(self):
        return self.count / len(self)

    loadFactor = property(
        fget = lambda self: self.getLoadFactor())
