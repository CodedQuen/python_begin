class Sorter(Object):

    def __init__(self):
        super(Sorter, self).__init__()
        self._array = None
        self._n = 0

    def _sort(self):
        pass
    _sort = abstractmethod(_sort)

    def sort(self, array):
        assert isinstance(array, Array)
        self._array = array
        self._n = len(array)
        if self._n > 0:
            self._sort()
        self._array = None

    def swap(self, i, j):
        tmp = self._array[i]
        self._array[i] = self._array[j]
        self._array[j] = tmp
