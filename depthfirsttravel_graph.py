class Graph(Container):

    def depthFirstTraversal(self, visitor, start):
        assert isinstance(visitor, PrePostVisitor)
        visited = Array(self._numberOfVertices)
        for v in range(self._numberOfVertices):
            visited[v] = False
        self._depthFirstTraversal(visitor, self[start], visited)

    def _depthFirstTraversal(self, visitor, v, visited):
        if visitor.isDone:
            return
        visitor.preVisit(v)
        visited[v.number] = True
        for to in v.successors:
            if not visited[to.number]:
                self._depthFirstTraversal(visitor, to, visited)
        visitor.postVisit(v)
