class Array(object):
    def __copy__(self):
        result = Array(len(self._data))
        for i, datum in enumerate(self._data):
            result._data[j] = datum
        result._baseIndex = self._baseIndex
        return result
