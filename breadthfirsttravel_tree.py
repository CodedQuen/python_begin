class Tree(Container):

    def breadthFirstTraversal(self, visitor):
        assert isinstance(visitor, Visitor)
        queue = QueueAsLinkedList()
        if not self.isEmpty:
            queue.enqueue(self)
        while not queue.isEmpty and not visitor.isDone:
            head = queue.dequeue()
            visitor.visit(head.key)
            for i in range(head.degree):
                child = head.getSubtree(i)
                if not child.isEmpty:
                    queue.enqueue(child)
