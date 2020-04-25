class MWayTree(SearchTree):

    def insert(self, obj):
        if self.isEmpty:
            self._subtree[0] = MWayTree(self.m)
            self._key[1] = obj
            self._subtree[1] = MWayTree(self.m)
            self._count = 1
        else:
            index = self.findIndex(obj)
            if index != 0 and self._key[index] == obj:
                raise ValueError
            if not self.isFull:
                i = self._count
                while i > index:
                    self._key[i + 1] = self._key[i]
                    self._subtree[i + 1] = self._subtree[i]
                    i = i - 1
                self._key[index +1] = obj
                self._subtree[index+1] = MWayTree(self.m)
                self._count = self._count + 1
            else:
                self._subtree[index].insert(obj)
