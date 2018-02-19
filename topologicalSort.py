
# this tompolical sort is based on the directedDfsRe code ( the recursive part is Robert code :(
import Digraph


class topologicalSort:
    stack = []
    path = {}
    postorder = []

    def __init__(self, digraph, root):

        self.Numnode = digraph.getNumNodes()
        #self.path[root] = root
        self.visited = self.Numnode * [False]
        self.check(digraph)
        self.dfs(digraph,root)


    def dfs(self, digraph,root):

        self.visited[root] = True
        nodesList = digraph.getEdges(root)
        for i in nodesList:
            if not self.visited[i]:
                self.dfs(digraph,i)
                self.path[i] = root
                self.postorder.append(i)


    def check(self, digraph):
        for i in digraph.getNodes():
            if not self.visited[i]:
                self.dfs(digraph,i)
                self.postorder.append(i)





