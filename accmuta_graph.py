class Graph(Container):

    def addVertex(self, *args): pass
    addVertex = abstractmethod(addVertex)

    def getVertex(self, v): pass
    getVertex = abstractmethod(getVertex)

    def addEdge(self, *args): pass
    addEdge = abstractmethod(addEdge)

    def getEdge(self, v, w): pass
    getEdge = abstractmethod(getEdge)

    def isEdge(self, v, w): pass
    isEdge = abstractmethod(isEdge)

    def depthFirstTraversal(self, visitor, start): pass
    depthFirstTraversal = abstractmethod(depthFirstTraversal)

    def breadthFirstTraversal(self, visitor, start): pass
    breadthFirstTraversal = abstractmethod(breadthFirstTraversal)

    def getIncidentEdges(self, v): pass
    getIncidentEdges = abstractmethod(getIncidentEdges)

    def getEmanatingEdges(self, v): pass
    getEmanatingEdges = abstractmethod(getEmanatingEdges)

    def __len__(self):
        return self.numberOfVertices

    def __getitem__(self, v):
        return self.getVertex(v)
