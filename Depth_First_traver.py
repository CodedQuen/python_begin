class Tree(Container):

    def depthFirstTraversal(self, visitor):
        assert isinstance(visitor, prePostVisitor)
        if not self.isEmpty and not visitor.isDone:
            visitor.preVisit(self.key)
            for i in range(self.degree):
                self.getSubtree(i).depthFirstTraversal(visitor)
            visitor.postVisit(self.key)
