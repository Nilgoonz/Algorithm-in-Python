class Digraph():

    node = []
    directedEdge = {}
    totall_nodes = 0
    def __init__(self,node):

        self.totall_nodes= node
        self.node = range(0, node)

    def addNode(self,node):

        self.totall_nodes = self.totall_nodes+1
        self.node.append(node)
    def getNodes(self):

        return self.node
    def getNumNodes(self):

        return self.totall_nodes

    def getEdges(self,node):
        return self.directedEdge.get(node,[])


    def addEdge(self,node1,node2):

        temp = self.directedEdge.get(node1,[])
        temp.append(node2)
        self.directedEdge[node1] = temp



