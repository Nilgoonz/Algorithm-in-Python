import graph

# note the original graph should be connected ( otherwise the path_length is not meaningful)

class bfs:
    def __init__(self, graph, r):
        self.path_length = {}
        self.nodes = []
        self.visited = {}
        self.qu = []
        self.root = r
        self.gr=graph
        self.gr=graph
        self.nodes = self.gr.getNode()
        self.qu = [r]
        self.path_length[r] = 0
        self.root = r
        for i in range(len(self.nodes)):
            self.visited[self.nodes[i]] = False
            self.visited[self.root] = True

    def run (self):
        while (len(self.qu) != 0):
            deQu = self.qu[0]
            adj_nodes = self.gr.getEdge(deQu)
            path = self.path_length.get(deQu, 0)
            self.qu.remove(deQu)
            self.__check(adj_nodes, path)


    def __check(self, list_nodes, path):
        for i in range(len(list_nodes)):
            if not self.visited[list_nodes[i]]:
                self.visited[list_nodes[i]] = True
                self.path_length[list_nodes[i]] = path + 1
                self.qu.append(list_nodes[i])

