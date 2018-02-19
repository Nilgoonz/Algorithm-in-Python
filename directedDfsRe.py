import Digraph
# this is a very nice and concise code that I stole from Robert online course

class directedDfs:
    stack = []
    path = {}

    def __init__(self, digraph, root):

        self.stack.insert(0, root)
        self.Numnode = digraph.getNumNodes()
        self.path[root] = root
        self.visited = self.Numnode * [False]
        self.dfs(digraph,root)

    def dfs(self, digraph,root):

            self.visited[root] = True
            nodelist = digraph.getEdges(root)
            for i in nodelist:
                if not self.visited[i]:
                    self.dfs(digraph, i)
                    self.path[i] = root






