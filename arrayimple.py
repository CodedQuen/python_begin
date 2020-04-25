class StackAsArray(Stack):

    def __init__(self, size = 0):
        super(StackAsArray, self).__init__()
        self._array = Array(size)

    def purge(self):
        while self._count > 0:
            self._array[self._count] = None
            self._count -= 1
            
