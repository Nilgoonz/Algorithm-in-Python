
import weightedEdgeGraph
import weightedEdge
import MSTkruskal

Wg = weightedEdgeGraph.weightedEdgeGraph(8)
Wg.addEdge(weightedEdge.weightedEdge(2,3,0.17))
Wg.addEdge(weightedEdge.weightedEdge(0,7,0.16))
Wg.addEdge(weightedEdge.weightedEdge(1,7,0.19))
Wg.addEdge(weightedEdge.weightedEdge(0,2,0.26))
Wg.addEdge(weightedEdge.weightedEdge(5,7,0.28))
Wg.addEdge(weightedEdge.weightedEdge(1,3,0.29))
Wg.addEdge(weightedEdge.weightedEdge(1,5,0.32))
Wg.addEdge(weightedEdge.weightedEdge(2,7,0.34))
Wg.addEdge(weightedEdge.weightedEdge(4,5,0.35))
Wg.addEdge(weightedEdge.weightedEdge(1,2,0.36))
Wg.addEdge(weightedEdge.weightedEdge(4,7,0.37))
Wg.addEdge(weightedEdge.weightedEdge(0,4,0.38))
Wg.addEdge(weightedEdge.weightedEdge(6,2,0.40))
Wg.addEdge(weightedEdge.weightedEdge(3,6,0.52))
Wg.addEdge(weightedEdge.weightedEdge(6,0,0.58))
Wg.addEdge(weightedEdge.weightedEdge(6,4,0.93))


MST = MSTkruskal.MSTkruskal(Wg)
print len(MST.MSTList)
lis= MST.MSTList
pvot= lis[6]
print pvot.weight


for i in range(len(MST.MSTList)):
    pvot=MST.MSTList[i]
    print pvot.weight