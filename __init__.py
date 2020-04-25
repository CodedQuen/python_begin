class Array(object):
    def __init__(self, length = 0, baseIndex = 0):
        assert length >= 0
        self._data = [None for i in range(length)]
        self._baseIndex = baseIndex
