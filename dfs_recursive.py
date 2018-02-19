# write dfs with recursion
# import graph


class dfs:
    def __init__(self, graph, r):
        self.node = graph.getNode()
        self.visited = {}
        self.path = {}
        for i in self.node:
            self.visited[i] = False
        self.stack = []
        self.stack.append(r)
        self.path[r] = 0
        self.oldPath = 0

    def dfs(self,graph, r):
        self.visited[r] = True
        for j in graph.getEdge(r):
            if not self.visited[j]:
                self.dfs(graph,j)
                self.path[j] = r
        self.path[r] = 0