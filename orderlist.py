class OrderedList(SearchableContainer):

    def __init__(self):
        super(OrderedList, self).__init__()

    def __getitem__(self, i):
        pass
    __getitem__ = abstractmethod(__getitem__)

    def findPosition(self, obj):
        pass
    findPosition = abstractmethod(findPosition)
