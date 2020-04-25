class DepthFirstSolver(Solver):

    def __init__(self):
        super(DepthFirstSolver, self).__init__()

    def search(self, current):
        if current.isComplete:
            self.updateBest(current)
        else:
            for successor in current.successors:
                self.search(successor)
