class BubbleSorter(Sorter):

    def __init__(self):
        super(BubbleSorter, self).__init__()

    def _sort(self):
        i = self._n
        while i > 1:
            for j in range(i - 1):
                if self._array[j] > self._array[j + 1]:
                    self.swap(j, j+ 1)
            i -= 1
