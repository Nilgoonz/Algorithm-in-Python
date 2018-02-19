import dfs_recursive

import graph

gr=graph.graph(7)
gr.addEdge(0,1)
gr.addEdge(0,2)
gr.addEdge(0,6)
gr.addEdge(6,4)
gr.addEdge(4,3)
gr.addEdge(4,5)
gr.addEdge(3,5)
gr.addEdge(5,0)


dfs2 = dfs_recursive.dfs(gr,0)
dfs2.dfs(gr,0)
print dfs2.path

#{0: 0, 1: 0, 2: 0, 3: 4, 4: 6, 5: 3, 6: 0}

#{0: 0, 1: 0, 2: 1, 3: 5, 4: 3, 5: 6, 6: 2}

# gr=graph.graph(5)
# gr.addEdge(1,2)
# gr.addEdge(1,3)
# gr.addEdge(1,5)
# gr.addEdge(2,3)
# gr.addEdge(2,4)
# gr.addEdge(2,5)
# gr.addEdge(3,4)
# gr.addEdge(3,5)
#
# dfs2 = dfs_recursive.dfs(gr,1)
# dfs2.dfs(gr,1)
#print dfs2.path