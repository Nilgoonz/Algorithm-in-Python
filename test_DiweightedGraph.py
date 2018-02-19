import DiWeightedEdgeGraph as DiWeight
import DiWeightedEdge

Di = DiWeight.DiWeightedEdgeGraph(2)
Di.addEdge(DiWeightedEdge.DiWeightedEdge(2,3,17))

temp= Di.Edges

closest = temp.index(min(temp))

print closest

temp2= temp[0]

print temp2.fromm()

