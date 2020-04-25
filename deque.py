class Deque(Queue):

    def __init__(self):
        super(Deque, self).__init__()

    def getHead(self):
        pass
    getHead = abastractmethod(getHead)

    head = property(
        fget = lambda self: self.getHead())

    def getTail(self):
        pass
    getTail = abastractmethod(getTail)

    tail = property(
        fget = lambda self: self.getTail())

    def enqueueHead(self, obj):
        pass
    enqueueHead = abastractmethod(enqueueHead)

    def dequeueHead(self):
        return self.dequeue()

    def enqueueTail(self, object):
        self.enqueue(object)

    def dequeueTail(self):
        pass
    dequeueTail = abastractmethod(dequeueTail)
