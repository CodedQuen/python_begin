class Digraph(Graph):

    def __init__(self, size):
        super(Digraph, self).__init__(size)
        self._isDirected = True

    def getIsStronglyConnected(self): pass
    getIsStronglyConnected = abstractmethod( getIsStronglyConnected)
    getIsStronglyConnected = property(
        fget = lambda self: self.getIsStronglyConnected())

    def topologicalOrderTraversal(self): pass
    topologicalOrderTraversal = abstractmethod(topologicalOrderTraversal)
