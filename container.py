class Container(Object):

    def __init__(self):
        super(Container, self).__init__()
        self._count = 0

    def purge(self):
        pass
    purge = abstractmethod(purge)

    def __iter__(self):
        pass
    __iter__ = abstractmethod(__iter__)
