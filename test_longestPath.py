import graph
import logestPath as lp
import findloop as fl

#gr=graph.graph(7)
#gr.addEdge(0,1)
#gr.addEdge(1,2)
#gr.addEdge(2,3)
#gr.addEdge(2,5)
#gr.addEdge(3,4)
#gr.addEdge(5,6)

gr=graph.graph(6)
gr.addEdge(0,1)
gr.addEdge(1,2)
gr.addEdge(2,3)
gr.addEdge(3,4)
gr.addEdge(4,5)
gr.addEdge(0,5)

# test = lp.longestPath(gr,0)

fl.findloop(gr,0)
