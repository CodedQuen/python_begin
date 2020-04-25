class Iterator(Object):

    def __init__(self, containter):
        super(Object, self).__init__()
        self._container = containter

    def __iter__(self):
        return self

    def next(self):
        pass

    next = abstractmethod(next)
