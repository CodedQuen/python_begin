
class BreadthFirstSolver(Solver):

    def __init__(self):
        super(BreadthFirstSolver, self).__init__()

    def search(self, initial):
        queue = QueueAsLinkedList()
        queue.enqueue(initial)
        while not queue.isEmpty:
            current = queue.dequeue()
            if current.isComplete:
                self.updateBest(current)
            else:
                for soln in current.successors:
                    queue.enqueue(soln)
