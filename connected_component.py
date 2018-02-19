import graph


class CC:
    nodes = []
    visited = {}
    path_length = {}
    qu = []
    root = 0
    gr = graph

    def __int__(self, graph, r):
        self.gr = graph
        self.nodes = self.gr.getNode()
        self.qu = [r]
        print self.qu
        self.path_length[r] = 0
        self.root = r
        for i in range(len(self.nodes)):
            self.visited[self.nodes[i]] = False
            self.visited[self.root] = True

    def run(self):
        def __check(list_nodes, path):
            for i in range(len(list_nodes)):
                if not self.visited[list_nodes[i]]:
                    self.visited[list_nodes[i]] = True
                    self.path_length[list_nodes[i]] = path + 1
                    self.qu.append(list_nodes[i])

        while (len(self.qu) != 0):
            deQu = self.qu[0]
            adj_nodes = self.gr.getEdge(deQu)
            path = self.path_length.get(deQu, 0)
            __check(adj_nodes, path)
            self.qu.remove(deQu)


