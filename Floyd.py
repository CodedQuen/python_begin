class Algorithms(object):

    def FloydsAlgorithm(g):
        n = g.numberOfVertices
        distance = DenseMatrix(n, n)
        for v in range(n):
            for w in range(n):
                distance[v, w] = sys.maxint
        for e in g.edges:
            distance[e.v0.number, e.v1.number] = e.weight
        for i in range(n):
            for v in range(n):
                for w in range(n):
                    if distance[v, i] != sys.maxint and \
                        distance[i, w] != sys.maxint:
                        d = distance[v, i] + distance[i, w]
                        if distance[v, w] > d:
                            distance[v, w] = d
        result = DigraphAsMatric(n)
        for v in range(n):
            result.addVertex(v)
        for v in range(n):
            for w in range(n):
                if distance[v, w] != sys.maxint:
                    result.addEdge(v, w, distance[v,w])
        return result
    FloydsAlgorithm = staticmethod(FloydsAlgorithm)
