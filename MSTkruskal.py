import weightedEdgeGraph
import QUnion

class MSTkruskal():

    def __init__(self,weightedGraph):

        self.Edges =weightedGraph.Edges
        self.SortedEdge = sorted(self.Edges)
        self.numNodes = weightedGraph.NumnNodes
        self.QU=QUnion.QuickFind(self.numNodes)
        self.MSTList = []
        self.__MST(self.SortedEdge)


    def __MST(self,list):
        nodeList=[]
        for i in list:
            either = i.either()
            other = i. other(either)
            if (not self.QU.find( either,other) and len(self.MSTList)<self.numNodes-1) :
                self.QU.union(either,other)
                self.MSTList.append(i)

