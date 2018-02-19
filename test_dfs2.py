import dfs2 as Al
import graph

# gr=graph.graph(5)
# gr.addEdge(1,2)
# gr.addEdge(1,3)
# gr.addEdge(1,5)
# gr.addEdge(2,3)
# gr.addEdge(2,4)
# gr.addEdge(2,5)
# gr.addEdge(3,4)
# gr.addEdge(3,5)

# ###
gr=graph.graph(7)

gr.addEdge(0,1)
gr.addEdge(0,2)
gr.addEdge(0,6)
gr.addEdge(5,0)
gr.addEdge(6,4)
gr.addEdge(4,3)
gr.addEdge(4,5)
gr.addEdge(3,5)



df=Al.dfs(gr,0)
#df.run(gr)

print df.path



