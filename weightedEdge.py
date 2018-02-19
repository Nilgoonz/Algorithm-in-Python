
class weightedEdge():


    def __init__(self,node1,node2,weight):
        self.weight = weight
        self.node1 = node1
        self.node2 = node2

    def either (self):
        return(self.node1)

    def other(self,node):
        if self.node1 == node: return self.node2
        else: return self.node1
    def __lt__ (self, other):
        return self.weight < other.weight

    def __gt__ (self, other):
        return other.__lt__(self)

    def __eq__ (self, other):
        return self.weight == other.weight

    def __ne__ (self, other):
        return not self.__eq__(other)