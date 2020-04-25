class Object(object):

    def __init__(self):
        super(Object, self).__init__()

    def __cmp__(self, obj):
        if isinstance(self, obj.__class__):
            return self._compareTo(obj)
        elif isinstance(obj, self.__class__):
            return -obj._compareTo(self)
        else:
            return cmp(self.__class__.__name__, obj.__class__.__name__)

    def _compareTo(self, obj):
        pass
    _compareTo = abstractmethod(_compareTo)
