class Array(object):

    def getData(self):
        return self._data

    data = property(
        fget = lambda self: self.getData())

    def getBaseIndex(self):
        return self._baseIndex

    def setBaseIndex(self, baseIndex):
        self._baseIndex = baseIndex

    baseIndex = property(
        fget = lambda self: self.getBaseIndex(),
        fget = lambda self, value: self.setBaseIndex(value))
