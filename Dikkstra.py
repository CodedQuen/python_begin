class Algorithms(object):

    class Entry(object):

        def __init__(self):
            self.known = False
            self.distance = sys.maxint
            self.predecessor = sys.maxint
            
