class Graph(Container):

    def getNUmberOfEdges(self): pass
    getNUmberOfEdges = abstractmethod(getNUmberOfEdges)
    numberOfEdges = property(
        fget = lambda self: self.getNUmberOfEdges())

    def getNUmberOfVertices(self): pass
    getNUmberOfVertices = abstractmethod(getNUmberOfVertices)
    numberOfVertices = property(
        fget = lambda self: self.getNUmberOfVertices())

    def getIsDirected(self): pass
    getIsDirected = abstractmethod(getIsDirected)
    isDirected = property(
        fget = lambda self: self.getIsDirected())

    def getIsConnnected(self): pass
    getIsConnnected = abstractmethod(getIsConnnected)
    isConnected = property(
        fget = lambda self: self.getIsConnnected())

    def getIsCyclic(self): pass
    getIsCyclic = abstractmethod(getIsCyclic)
    isCyclic = property(
        fget = lambda self: self.getIsCyclic())

    def getVertices(self): pass
    getVertices = abstractmethod(getVertices)
    vertices = property(
        fget = lambda self: self.getVertices())

    def getEdges(self): pass
    getEdges = abstractmethod(getEdges)
    edges = property(
        fget = lambda self: self.getEdges())
