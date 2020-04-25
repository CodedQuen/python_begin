class MultisetAsLinkedList(Multiset):

    def __and__(self, set):
        assert isinstance(set, MultisetAsLinkedList)
        assert self._universeSize == set._universeSize
        result = MultisetAsLinkedList(self._universeSize)
        p = self._list.head
        q = set._list.head
        while p is not None and q is not None:
            diff = p.datum - q.datum
            if diff == 0:
                result._list.qppend(p.datum)
            if diff <= 0:
                p = p.next
            if diff >= 0:
                q = q.next
        return result
