class DiWeightedEdge:

    def __init__(self,fromm,to,weight):
        self.v = fromm
        self.w = to
        self.weight = weight

    def fromm(self):
        return self.v

    def to(self):
        return self.w

    def weight(self):
        return self.weight

    def __lt__ (self, other):
        return self.weight < other.weight

    def __gt__ (self, other):
        return other.__lt__(self)

    def __eq__ (self, other):
        return self.weight == other.weight

    def __ne__ (self, other):
        return not self.__eq__(other)



