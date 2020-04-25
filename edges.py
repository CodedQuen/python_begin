class Edge(Object):

    def __init__(self):
        super(Edge, self).__init__()

    def getVO(self): pass
    getVO = abstractmethod(getVO)
    vO = property(
        fget = lambda self: self.getVO())

    def getV1(self): pass
    getV1 = abstractmethod(getV1)
    v1 = property(
        fget = lambda self: self.getV1())

    def getWeight(self): pass
    getWeight = abstractmethod(getWeight)
    weight = property(
        fget = lambda self: self.getWeight())

    def getIsDirected(self): pass
    getIsDirected = abstractmethod(getIsDirected)
    isDirected = property(
        fget = lambda self: self.getIsDirected())

    def mateOf(self, vertex): pass
    mateOf = abstractmethod(mateOf)
