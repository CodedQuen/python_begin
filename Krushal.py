class Algorithms(object):

    def KruskalsAlgorithms(g):
        n = g.numberOfVertices
        result = GraphAsLists(n)
        for v in range(n):
            result.addVertex(v)
        queue = BinaryHeap(g.numberOfEdges)
        for e in g.edges:
            weight = e.weight
            queue.enqueue(Association(weight, e))
        partition = PartitionAsForest(n)
        while not queue.isEmpty and partition.count > 1:
            assoc = queue.dequeueMin()
            e = assoc.value
            n0 = e.v0.number
            n1 = e.v1.number
            s = partition.find(n0)
            t = partition.find(n1)
            if s != t:
                partition.join(s, t)
                result.addEdge(n0, n1)
        return result
    KruskalsAlgorithms = staticmethod(KruskalsAlgorithms)
