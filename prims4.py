import weightedEdgeGraph

class prims():

    def __init__(self, WG):

        self.NumNodes = WG.NumnNodes
        self.r = 0
        self.edgeList = WG.getEdge(0)
        self.visited = {}
        self. MST = []
        for i in range(self.NumNodes):
            self.visited[i] = False
        self.visited[0] = True
        self.__primss(WG)

    def __primss(self,WG):

        while(len(self.MST)< self.NumNodes-1):
            self.sorted = sorted(self.edgeList)
            EdgeMin = self.sorted[0]
            either = EdgeMin.either()
            other = EdgeMin.other(either)
            self.edgeList = filter(lambda x: x != EdgeMin, self.edgeList)

            if self.visited[other] and self.visited[either]:
                continue

            else:
                self.visited[either] = True
                self.visited[other] = True
                self.MST.append(EdgeMin)
                self.edgeList = self.edgeList + WG.getEdge(other) + WG.getEdge(either)






