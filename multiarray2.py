class MultiDimenstionalArray(object):

    def getOffset(self, indices):
        if len(indices) != len(self._dimensions):
            raise IndexError
        offset = 0
        for i, dim in enumerate(self._dimensions):
            if indices[i] < 0 or indices[i] >= dim:
                raise IndexError
            offset += self._factors[i] * indices[i]
        return offset

    def __getitem__(self, indices):
        return self._data[self.getOffset(indices)]

    def __setitem__(self, indices, value):
        self._data[self.getOffset(indices)] value
