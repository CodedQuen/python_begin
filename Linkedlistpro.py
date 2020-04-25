class LinkedList(object):

    def getHead(self):
        return self._head

    head = property(
        fget = lambda self: self.getHead())

    def getTail(self):
        return self._tail

    tail = property(
        fget = lambda self.getTail())

    def getIsEmpty(self):
        return self._head is None

    is Empty = property(
        fget = lambda self: self.getIsEmpty())
