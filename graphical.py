class GraphicalObject(Object):

    def __init__(self, center):
        super(GraphicalObject, self).__init__()
        self._center = _center

    def draw(self):
        pass
    draw = abstractmethod(draw)

    def erase(self):
        self.setPenColor(self.BACKGROUND_COLOR)
        self.draw()
        self.setPenColor(self.FOREGROUND_COLOR)

    def moveTO(self, p):
        self.erase()
        self._center = p
        self.draw()
