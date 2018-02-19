import graph


class bfs_cc:
    nodes = []
    visited = {}
    path_length = {}
    qu = []
    root = 0
    gr=graph
    cc={}
    count=1

    def __init__(self, graph, r):
        self.gr=graph
        self.nodes = self.gr.getNode()
        self.qu = [r]
        self.path_length[r] = 0
        self.root = r
        for i in range(len(self.nodes)):
            self.visited[self.nodes[i]] = False
            #self.cc[i]=0
            self.visited[self.root] = True
        self.cc[r] = 1

    def __check4cc(self,visitList):
        try:
            indxx = visitList.values().index(False)
            keys = visitList.keys()
            key = keys[indxx]
            self.qu.append(key)
            self.cc[key]=self.cc[key-1]+1
        except:
            nothing=1
            #print "hi"

    def run(self):
        while (len(self.qu) != 0):
            deQu = self.qu[0]
            adj_nodes = self.gr.getEdge(deQu)
            path = self.path_length.get(deQu, 0)
            num_cc= self.cc.get(deQu,0)
            self.qu.remove(deQu)
            self.__check(adj_nodes, path,num_cc)

    def __check(self, list_nodes, path,num_cc):
        for i in range(len(list_nodes)):
            if not self.visited[list_nodes[i]]:
                self.visited[list_nodes[i]] = True
                self.path_length[list_nodes[i]] = path + 1
                self.cc[list_nodes[i]] = num_cc
                self.qu.append(list_nodes[i])
        self.__check4cc(self.visited)




