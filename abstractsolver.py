class Solver(Object):

    def __init__(self):
        super(Solver, self).__init__()
        self._bestSolution = None
        self._bestObjective = sys.maxint

    def search(self, initial):
        pass
    search = abstractmethod(search)

    def solve(self, initial):
        assert isinstance(initial, Solution)
        self._bestSolution = None
        self._bestObjective = sys.maxint
        self.search(initial)
        return self._bestSolution

    def updateBest(self, solution):
        if solution.isComplete and solution.isFeasible and \
                solution.objective < self._bestObjective:
            self._bestSolution = sulution
            self._bestObjective = solution.objective
