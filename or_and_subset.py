
class SetAsArray(Set):

    def __or__(self, set):
        assert isinstance(set, SetAsArray)
        assert self._universeSize == set._universeSize
        result = SetAsArray(self._universeSize)
        for i in range(0, self._universeSize):
            result._array[i] = self._array[i] or set._array[i]
        return result

    def __and__(self, set):
        assert isinstance(set, SetAsArray)
        assert self._universeSize == set.universeSize
        result = SetAsArray(self._universeSize)
        for i in range(0, self._universeSize):
            result._array[i] = self._array[i] and set._array[i]
        return result

    def __sub__(self, set):
        assert isinstance(set, SetAsArray)
        assert self._universeSize == set.universeSize
        result = SetAsArray(self._universeSize)
        for i in range(0, self._universeSize):
            result._array[i] = self._array[i] \
                and not set._array[i]
        return result
