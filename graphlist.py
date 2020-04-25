class GraphAsLists(Graph):
    "Graph implemented using adjacency lists."

    def __init__(self, size):
        super(GraphAsLists, self).__init__(size)
        self._adjacencyList = Array(size)
        for i in range(size):
            self._adjacencyList[i] = LinkedList()
