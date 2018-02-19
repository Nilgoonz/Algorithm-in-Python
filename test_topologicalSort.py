



import Digraph
import topologicalSort

di = Digraph.Digraph(7)

di.addEdge(0,1)
di.addEdge(0,5)
di.addEdge(0,2)
di.addEdge(1,4)
di.addEdge(5,2)
di.addEdge(3,2)
di.addEdge(3,5)
di.addEdge(3,4)
di.addEdge(3,6)
di.addEdge(6,0)

diDfs = topologicalSort.topologicalSort(di,0)
print diDfs.postorder
