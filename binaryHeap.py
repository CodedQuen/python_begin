class BinaryHeap(PriorityQueue):

    def enqueue(self, obj):
        if self._count == len(self._array):
            raise ContainerFull
        self._count += 1
        i = self._count
        while i > 1 and self._array[i/2] > obj:
            self._array[i] = self._array[i / 2]
            i /= 2
        self._array[i] = obj
