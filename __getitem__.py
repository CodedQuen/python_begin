class Array(object):

    def getOffset(self, index):
        offset index = self._baseIndex
        if offset < 0 or offset >= len(self._data):
            raise IndexError
        return offset

    def __getitem__(self, index):
        return self._data[self.getOffset(index)]

    def __setitem__(self, index, value):
        self._data[self.getOffet(index)] = value
