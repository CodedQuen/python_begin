class InOrder(PrePostVisitor):

    def __init__(self, visitor):
        super(InOrder, self).__init__()
        self._visitor = visitor

    def inVisit(self, obj):
        self._visitor.visit(obj)

    def getIsDone(self):
        return self._visitor.isDone 
