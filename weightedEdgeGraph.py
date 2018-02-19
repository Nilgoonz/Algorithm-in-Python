
import weightedEdge
import itertools
class weightedEdgeGraph():

    def __init__(self,NumnNodes):
        self.adjList={}
        self.Edges=[]
        self.NumnNodes=NumnNodes

    def addEdge(self,WE):
        node1 = WE.either()
        node2 = WE.other(node1)
        temp = self.adjList.get(node1,[])
        temp.append(WE)
        self.adjList[node1]=temp
        temp1= self.adjList.get(node2,[])
        temp1.append(WE)
        self.adjList[node2] = temp1
        self.Edges.append(WE)


    def getEdge(self,node):
        return self.adjList.get(node)

    def NumnNodes(self):
        return self.NumnNodes

