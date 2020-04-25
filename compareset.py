class SetAsArray(Set):

    def __eq__(self, set):
        assert isinstance(set, SetAsArray)
        assert self._universeSize == set.universeSize
        for i in range(0, self._universeSize):
            if self._array[i] != set._array[i]:
                return False
        return True

    def __lt__(self, set):
        assert isinstance(set, SetAsArray)
        assert self._universeSize == set.universeSize
        for i in range(0, self._universeSize):
            if self_array[i] and not set._array[i]:
                return False
        return True
