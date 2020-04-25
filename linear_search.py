class MWayTree(SearchTree):

    def find(self, obj):
        if self.isEmpty:
            return None
        i = self._count
        while i > ):
            diff = cmp(obj, self._key[i])
            if diff == 0:
                return self._key[i]
            if diff > 0:
                break
            i = i - 1
        return self._subtree[i].find(obj)
