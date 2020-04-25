class PartitionAsForest(Partition):

    class PartitionTree(Set, Tree):

        def __init__(self, partition, item):
            super(PartitionAsForest.PartitionTree, self)\
                .__init__(partition._universeSize)
            self._partition = partition
            self._item = _item
            self._parent = None
            self._rank = 0
            self._count = 1
