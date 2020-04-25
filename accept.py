class StackAsArray(Stack):

    def accept(self, visitor):
        assert isinstance(visitor, Visitor)
        for i in range(self._count):
            visitor.visit(self._array[i])
            if visitor.isDone:
                return
