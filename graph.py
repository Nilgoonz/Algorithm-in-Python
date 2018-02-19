class graph:
    Node = []
    Edge = {}

    def __init__(self, n):
        self.Node = range(1, n+1)

    def getNode(self):
        return (self.Node)

    def getEdge(self, n):
        return (self.Edge.get(n, []))

    def addNode(self, n):
        self.Node.append(n)

    def addEdge(self, n, m):
        temp1 = self.Edge.get(n, [])
        temp1.append(m)
        temp2 = self.Edge.get(m, [])
        temp2.append(n)
        self.Edge[n] = temp1
        self.Edge[m] = temp2
