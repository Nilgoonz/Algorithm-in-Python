import DiWeightedEdge
import DiWeightedEdgeGraph

class Dijkstra:

    def __init__(self,DiWeGraph,N,source):

        self.DiWeGraph=DiWeGraph
        self.source = source
        self.NumNodes = N
        self.MST =[]
        self.pq = []
        self.edgeTo = {}
        self.distTo = ["inf"]* self.NumNodes

        self.distTo[self.source] = 0
        self.sourceStart = DiWeightedEdge.DiWeightedEdge(0,0,0)
        self.pq.append(self.sourceStart)
        self.__runDijkstra(self.distTo)


    def __runDijkstra(self,distTo):


        while len(self.pq)!= 0 :
            closest = self.pq.index(min(self.pq))
            minn = min(self.pq)
            #print minn.to()
            self.MST.append(min(self.pq))
            self.__relaxAllEdges(self.DiWeGraph,minn)
            del self.pq[closest]




    def __relaxAllEdges(self,DiWeGraph, closest):

        listEdge = DiWeGraph.getEdge(closest.to())

        for edge in listEdge:

            fromm = edge.fromm()
            to = edge.to()
            weight = edge.weight

            if self.distTo[to]>self.distTo[fromm]+weight:
                self.distTo[to] = self.distTo[fromm]+weight
                self.edgeTo[to] = edge
                self.pq.append(DiWeightedEdge.DiWeightedEdge(fromm,to,self.distTo[to]))







