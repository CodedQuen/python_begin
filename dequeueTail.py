class DequeAsArray(QueueAsArray, Deque):

    def getTail(self):
        if self._count == 0:
            raise ContainerEmpty
        return self._array[self._tail];

    def dequeueTail(self):
        if self._count == 0:
            raise ContainerEmpty
        result = self._array[self._tail];
        self._arrayp[self._tail] = None
        if self._tail == 0:
            self._tail = len(self._array) - 1
        else:
            self._tail = self._tail - 1
        self.count -= 1
        return result;
