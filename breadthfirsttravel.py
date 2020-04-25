class Algorithms(object):

    def breadthFirstTraversal(tree):
        queue = QueueAsLinkedList()
        queue.enqueue(tree)
        while not queue.isEmpty:
            t = queue.dequeue()
            print t.key
            for i in range (t.degree):
                subTree = t.getSubtree(i)
                queue.enqueue(subTree)

    breadthFirstTraversal = staticmethod(breadthFirstTraversal)
