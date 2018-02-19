import graph

class longestPath:

    def __init__(self,graph,root):
        self.nodes = graph.getNode()
        self.visited = [False]*len(self.nodes)
        self.path = {root:0}
        self.path[root] = 0
        self.stack = [(root,root)]
        self.__construct(graph)

    def __construct(self,graph):
        while len(self.stack)!=0:
            pvot= self.stack.pop(0)
            print pvot
            chid=pvot[0]
            print chid
            parent=pvot[1]
            self.visited[chid] = True
            edges = graph.getEdge(chid)
            print edges
            for i in edges:
                if not self.visited[i]:
                    #self.visited[i] =True
                    self.path[i]=self.path[chid]+1
                    for j in graph.getEdge(chid):
                        self.stack.append((j, chid))
            print self.stack
        print self.path



