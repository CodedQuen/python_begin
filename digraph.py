class Digraph(Graph):

    def topologicalOrderTraversal(self, visitor):
        inDegree = Array(self.numberOfVertices)
        for v in range(self.numberOfVertices):
            inDegree[v] = 0
        for e in self.edges:
            inDegree[e.v1.number] += 1
        queue = QueueAsLinkedList()
        for v in range(self.numberOfVertices):
            if inDegree[v] == 0:
                queue.enqueue(self[v])
        while not queue.isEmpty and not visitor.isDone:
            v = queue.dequeue()
            visitor.visit(v)
            for to in v.successors:
                inDegree[to.number] -= 1
                if inDegree[to.number] == 0:
                    queue.enqueue(to)
