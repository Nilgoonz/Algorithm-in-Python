import Digraph

Di1 = Digraph.digraph(5)
Di1.addEdge(0,1)
Di1.addEdge(0,5)
Di1.addEdge(0,2)
Di1.addEdge(3,2)
Di1.addEdge(3,4)
Di1.addEdge(3,5)
Di1.addEdge(3,6)
Di1.addEdge(5,2)
Di1.addEdge(6,0)



print Di1.getNumNodes()
print Di1.getEdges(5)


