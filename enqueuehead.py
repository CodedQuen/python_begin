class DequeAsArray(QueueAsArray, Deque):

    def __init__(self, size = 0):
        super(DequeAsArray, self).__init__(size)

    def enqueueHead(self, obj):
        if self._count == len(self._array):
            raise ContainerFull
        if self._head == 0:
            self._head = len(self._array) - 1
        else:
            self._head = self._head - 1
        self._array[self._head] = obj;
        self._count += 1
