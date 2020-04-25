class Matrix(object):

    def __init__(self, numberOfRows, numberOfColumns):
        assert numberOfRows >= 0
        assert numberOfColumns >= 0
        super(Matrix, self).__init__()
        self._numberOfRows = numberOfRows
        self._numberOfColumns = numberOfColumns

    def getNumberOfRows(self):
        return self._numberOfRows

    numberOfRows = property(
        fget = lambda self: self.getNumberOfRows())

    def getNumberOfColumns(self):
        return self._numberOfColumns

    numberOfColumns = property(
        fget = lambda self: self.getNumberOfColumns())

print(Matrix(1,2))
