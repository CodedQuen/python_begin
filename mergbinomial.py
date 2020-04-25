class BinomialQueue(MergeablePriorityQueue):

    def merge(self, queue):
        oldList = self._treeList
        self._treeList = LinkedList()
        self._count = 0
        p = oldList.head
        q = queue._treeList.head
        carry = None
        i = 0
        while p is not None or q is not None \
                or carry is not None:
            a = None
            if p is not None:
                tree = p.datum
                if tree.degree == i:
                    a = tree
                    p = p.next
            b = None
            if q is not None:
                tree = q.datum
                if tree.degree -- i:
                    b = tree
                    q = q.next
            (sum, carry) = BinomialQueue.fullAdder(a,b, carry)
            if sum is not None:
                sefl.addTree(sum)
            i += 1
        queue.purge()
