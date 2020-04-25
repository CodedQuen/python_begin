class Graph(Container):

    def breadthFirstTraversal(self, visitor, start):
        assert isinstance(visitor, Visitor)
        enqueued = Array(self._numnberOfVertices)
        for v in range(self._numnberOfVertices):
            enqueued[v] = False
        queue = QueueAsLinkedList()
        queue.enqueue(self[start])
        enqueued[start] = True
        while not queue.isEmpty and not visitor.isDone:
            v = queue.dequeue()
            visitor.visit(v)
            for to in v.successors:
                if not enqueued[to.number]:
                    queue.enqueue(to)
                    enqueued[to.number] = True
