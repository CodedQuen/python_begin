class QueueAsArray(Queue):

    def getHead(self):
        if self._count == 0:
            raise ContainerEmpty
        return self._array[self._head]

    def enqueue(self, obj):
        if self._count == len(self._array):
            raise ContainerFull
        self._tail = self._tail + 1
        if self._tail == len(self._array):
            self._tail = 0
        self._array[self._tail] = obj
        self._count += 1

    def dequeue(self):
        if self._count == 0:
            raise ContainerEmpty
        result = self._array[self._head]
        self._array[self._head] = None
        self._head = self._head + 1
        if self._head == len(self._array):
            self._head = 0
        self._count -= 1
        return result
