import DiWeightedEdge
import DiWeightedEdgeGraph
import Dijkstra


DiW = DiWeightedEdgeGraph.DiWeightedEdgeGraph(8)
DiW.addEdge(DiWeightedEdge.DiWeightedEdge(0,1,5))
DiW.addEdge(DiWeightedEdge.DiWeightedEdge(0,7,8))
DiW.addEdge(DiWeightedEdge.DiWeightedEdge(0,4,9))
DiW.addEdge(DiWeightedEdge.DiWeightedEdge(1,7,4))
DiW.addEdge(DiWeightedEdge.DiWeightedEdge(1,3,15))
DiW.addEdge(DiWeightedEdge.DiWeightedEdge(1,2,12))
DiW.addEdge(DiWeightedEdge.DiWeightedEdge(7,2,7))
DiW.addEdge(DiWeightedEdge.DiWeightedEdge(7,5,6))
DiW.addEdge(DiWeightedEdge.DiWeightedEdge(4,7,5))
DiW.addEdge(DiWeightedEdge.DiWeightedEdge(4,5,4))
DiW.addEdge(DiWeightedEdge.DiWeightedEdge(4,6,20))
DiW.addEdge(DiWeightedEdge.DiWeightedEdge(5,2,1))
DiW.addEdge(DiWeightedEdge.DiWeightedEdge(5,6,13))
DiW.addEdge(DiWeightedEdge.DiWeightedEdge(2,3,3))
DiW.addEdge(DiWeightedEdge.DiWeightedEdge(2,6,11))
DiW.addEdge(DiWeightedEdge.DiWeightedEdge(3,6,9))

Dij = Dijkstra.Dijkstra(DiW,8,0)

ed= Dij.edgeTo[2]

print ed.fromm()










