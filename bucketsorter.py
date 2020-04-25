class BucketSorter(Sorter):

    def _sort(self):
        for i in range(self._m):
            self._count[i] = 0
        for j in range(self._n):
            self._count[self._array[j]] += 1
        j = 0
        for i in range(self._m):
            while self._count[i] > 0:
                self._array[j] = i
                j += 1
                self._count[i] -= 1
