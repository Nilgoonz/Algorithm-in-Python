import Digraph


class directedDfs:
    stack = []
    visited = {}
    nodelist = []
    path = {}

    def __init__(self, digraph, root):

        self.stack.insert(0, (root, root))
        self.nodelist = digraph.getNumNodes()
        self.path[root] = root
        self.visited = self.nodelist * [False]
        self.__dfs(digraph)

    def __dfs(self, digraph):

        while len(self.stack) != 0:
            pvot = self.stack.pop(0)
            child = pvot[0]
            print child
            parent = pvot[1]
            if not self.visited[child]:
                self.visited[child] = True
                self.path[child] = parent
                edges = digraph.getEdges(child)
                for j in edges:
                    self.stack.insert(0, [j, child])
