

# find loop
import graph

class findloop:

    def __init__(self,graph,root):
        self.nodes = graph.getNode()
        self.visited = {}
        self.path = {root:0}
        self.path[root] = 0
        self.stack = [(root,0)]
        self.comefrom={root:0}
        self.__construct(graph)

    def __construct(self,graph):
        while len(self.stack)!=0:
            pvot= self.stack.pop(0)
            #print pvot
            chid=pvot[0]
            parent=pvot[1]
            self.visited[chid] = True
            edges = graph.getEdge(chid)
            print chid
            print parent
            print edges
            for i in edges:
                if self.visited.get(i, False) and not i == parent:
                    print self.visited
                    print self.comefrom
                    print i
                    print parent
                    print chid
                    return True
                if not self.visited.get(i, False):
                    self.comefrom[i] = chid
                    self.path[i]=self.path[chid]+1
                    self.stack.insert(0, (i, chid))
                    # for j in graph.getEdge(chid):
                    #     self.stack.insert(0,(j, chid))
        print self.comefrom



