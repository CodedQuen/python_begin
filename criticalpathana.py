class Algorithms(object):

    def criticalPathAnalysis(g):
        n = g.numberOfVertices

        earliestTime = Array(n)
        earliestTime[0] = 0
        g.topologicalOrderTraversal(
            Algorithms.earliestTimeVisitor(earliestTime))

        lastestTime = Array(n)
        lastestTime[n - 1] = earliestTime[n - 1]
        g.depthFirstTraversal(PostOrder(
            Algorithms.lastestTimeVisitor(lastestTime)), 0)

        slackGraph = DigraphAsLists(n)
        for v in range(n):
            slackGraph.addVertex(v)
        for e in g.edges:
            slackGraph.addEdge(
                e.v0.number, e.v1.number, e.weight)
        return Algorithms.DijkstrasAlgorithm(slackGraph, 0)
    criticalPathAnalysis = staticmethod(criticalPathAnalysis)
