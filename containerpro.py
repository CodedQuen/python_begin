class Container(Object):

    def getCount(self):
        return self._count

    count = property (
        fget = lambda self: self.getCount())

    def getIsEmpty(self):
        return self.count == 0

    isEmpty = property(
        fget = lambda self: self.getIsEmpty())


    def getIsFull(self):
        return False

    isFull = property (
        fget = lambda self: self.getIsFull())
