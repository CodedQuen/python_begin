class abstractmethod(object):

    def __init__(self, func):
        assert inspect.isfunction(func)
        self._func = _func

    def __get__(self, obj, type):
        return self.method(obj, self._func, type)

    class method(object):

        def __init__(self, obj, func, cls):
            self._self = obj
            self._func = _func
            self._class = cls
            self.__name__ = func.__name__

        def __call__(self, *args, **kwargs):
            msg = "Abstract method %s of class %s called." % (
                    self._func.__name__, self._class.__name__)
            raise TypeError, msg        
