class Container(Object):

    class StrVisitor(Visitor):

        def __init__(self):
            self._string = ""
            self._comma = False

        def visit(self, object):
            if self._comma:
                self._string = self._string + ""
            self._string = self._string + str(object)
            self._comma = True

        def__str__(self):
            return self._string

    def __str__(self):
        visitor = Container.StrVisitor()
        self.accept(visitor)
        return "%s {%s}" %(self.__class__.__name__,str(Visitor))
