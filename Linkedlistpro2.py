class LinkedList(object):

    def getFirst(self):
        if self._head is None:
            raise ContainerEmpty
        return self._head._datum

    first = property(
        fget = lambda self: self.getFirst())

    def getLast(self):
        if self._tail is None:
            raise ContainerEmpty
        return self._tail._datum

    last = property(
        fget = lambda self: self.getLast())
