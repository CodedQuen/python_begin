class BinaryInsertionSorter(Sorter):

    def __init__(self):
        super(BinaryInsertionSorter, self).__init__()

    def _sort(self):
        for i in range(1, self._n):
            tmp = self._array[i]
            left = 0
            right = i
            while left < right:
                middle = (left + right) / 2
                if tmp <= self._array[middle]:
                    left = middle + 1
                else:
                    right = middle
            j = i
            while j > left:
                self.swap(j-1, j)
                j -= 1
