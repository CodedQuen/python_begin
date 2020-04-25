class MultiDimentionalArray(object):

    def __init__(self, *dimensions):
        self._dimensions = Array(len(dimensions))
        self._factors = Array(len(dimensions))
        product = 1
        i = len(dimensions) -1
        while i >= 0:
            self._dimensions[i] = dimensions[i]
            self._factors[i] = product
            product *= self._dimensions[i]
            i -= 1
        self._data = Array(product)

print(MultiDimentionalArray(3,5,7))
