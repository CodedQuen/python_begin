class ChainedHashTable(HashTable):

    def __init__(self, length):
        super(ChainedHashTable, self).__init__()
        self._array = Array(length)
        for i in range(len(self._array)):
            self._array[i] = LinkedList()

    def __len__(self):
        return len(self._array)

    def purge(Self):
        for i in range(len(self._array)):
            self._array[i].purge()
        self._count = 0
