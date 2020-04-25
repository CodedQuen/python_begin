class DepthFirstBranchAndBoundSolver(Solver):

    def __init__(self):
        super(DepthFirstBranchAndBoundSolver, self).__init__()

    def search(self, current):
        if current.isComplete:
            self.updateBest(current)
        else:
            for successor in current.successors:
                if successor.isFeasible and \
                        successor.bound < self._bestObjective:
                            self.serach(successor)
