import Digraph
import directedDfs

di = Digraph.Digraph(7)

di.addEdge(0,1)
di.addEdge(0,5)
di.addEdge(2,0)
di.addEdge(2,3)
di.addEdge(3,2)
di.addEdge(3,5)
di.addEdge(4,2)
di.addEdge(4,3)
di.addEdge(5,4)
di.addEdge(6,0)
di.addEdge(6,4)
print di.getEdges(1)

diDfs = directedDfs.directedDfs(di,0)
print diDfs.path
