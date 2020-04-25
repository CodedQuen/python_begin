class Association(Object):

    def getKey(self):
        return self._tuple[0]

    key = property(
        fget = lambda self: self.getKey())

    def getValue(self):
        return self._tupel[1]

    value = property(
        fget = lambda self: self.getValue())
