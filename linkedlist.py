class LinkedList(object):

    class Element(object):

        def__init__(self, list, datum, next):
            self._list = list
            self._datum = datum
            self._next = next

        def getDatum(self):
            return self._datum

        datum = property(
            fget = lambda self: self.getDatum())

        def getNext(self):
            return self._next

        next = property(
            fget = lambda self: self.getNext())
