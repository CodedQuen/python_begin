class LinkedList(object):

    def append(self, item):
        tmp = self.Element(self, item, None)
        if self._head is None:
            self._head = tmp
        else:
            self._tail._next = tmp
        self._tail = tmp
