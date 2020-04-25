class MedianOfThreeQuickSorter(QuickSorter):

    def __init__(self):
        super(MedianOfThreeQuickSorter, self).__init__()

    def selectPivot(self, left, right):
        middle = (left + right) / 2
        if self._array[left] > self._array[middle]:
            self.swap(left, middle)
        if self._array[left] > self._array[right]:
            self.swap(left, right)
        if self._array[middle] > self._array[right]:
            self.swap(middle, right)
        return middle
