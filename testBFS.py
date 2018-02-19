import graph
import bfs
import dfs
import bfs_cc
# g=graph.graph(6)
# g.addEdge(1,2)
# g.addEdge(1,5)
# g.addEdge(1,4)
# g.addEdge(2,3)
# g.addEdge(3,4)
# g.addEdge(5,4)
# g.addEdge(4,6)
#
# bf = bfs.bfs(g,1)
# bf.run()
# print bf.path_length

h=graph.graph(7)
h.addEdge(1,2)
h.addEdge(1,5)
h.addEdge(1,4)
h.addEdge(2,3)
h.addEdge(3,4)
h.addEdge(5,4)
h.addEdge(6,7)

#bf=bfs.bfs(h,1)
#bf.run()
#print bf.path_length
#print h.getNode()
#print bf.visited.values().index(False)

#bf2=bfs_cc.bfs_cc(h,1)
#bf2.run()
#print bf2.cc

df = dfs.dfs(h,1)


