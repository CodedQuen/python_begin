class Cursor(Object):

    def __init__(self, list):
        super(Cursor, self).__init__()
        self._list = _list

    def getDatum(self):
        pass
    getDatum = abstractmethod(getDatum)

    datum = property(
        fget = lambda self: self.getDatum())

    def insertAfter(self, obj):
        pass
    insertAfter = abstractmethod(insertAfter)

    def insertBefore(self, obj):
        pass
    insertBefore = abstractmethod(insertBefore)

    def withdraw(self, obj):
        pass
    withdraw = abstractmethod(withdraw)
