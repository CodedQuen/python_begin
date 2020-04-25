class Partition(Set):

    def __init__(self, n):
        super(Partition, self).__init__(n)

    def find(self, obj):
        pass
    find = abstractmethod(find)

    def join(self, s, t):
        pass
    join = abstractmethod(join)
