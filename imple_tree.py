class Tree(Container):

    def getKey(self):
        pass
    getKey = abstractmethod(getKey)

    key = property(
        fget = lambda self: self.getKey())

    def getSubtree(self, i):
        pass
    getSubtree = abstractmethod(getSubtree)

    def getIsLeaf(self):
        pass
    getIsLeaf = abstractmethod(getIsLeaf)

    isLeaf = property(
        fget = lambda self: self.getIsLeaf())

    def getDegree(self):
        pass
    getDegree = abstractmethod(getDegree)

    degree = property(
        fget = lambda self: self.getDegree())

    def getHeight(self):
        pass
    getHeight = abstractmethod(getHeight)

    height = property(
        fget = lambda self: self.getHeight())
