
import DiWeightedEdge
class DiWeightedEdgeGraph:

    def __init__(self,N):
        self.numNodes = N
        self.Edges=[]
        self.adjList = {}

    def addEdge(self,DiWeightedEdge):
        startNode = DiWeightedEdge.fromm()
        EdgeList = self.adjList.get(startNode,[])
        EdgeList.append(DiWeightedEdge)
        self.adjList[startNode] = EdgeList
        self.Edges.append(DiWeightedEdge)

    def getEdge(self,Node):
        return self.adjList.get(Node,[])

