import graph as gr

g = gr.graph(3)
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(2,3)

print (g.getEdge(2))
g.addNode(5)
print g.getNode()


