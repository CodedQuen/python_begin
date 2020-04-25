class PostOrder(PrePostVisitor):

    def __init__(self, visitor):
        super(PostOrder, self).__init__()
        self._visitor = visitor

    def postVisit(self, obj):
        self._visitor.visit(obj)

    def getIsDone(self):
        return self._visitor.isDone 
