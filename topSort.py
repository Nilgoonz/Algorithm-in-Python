
import graph
import Digraph

class topSort:

    def __init__(self,Digraph,r):
        self.nodes = Digraph.getNodes()
        self.visited = {}
        self.path={}
        for i in self.nodes :
            self.visited[i] = False
        for i in self.nodes :
            self.path[i] = ""

        self.stack = []
        self.edges = graph.getEdges(r)
        self.path[r] = 0
        self.visited[r] = True

        def run(self):
            for j in range(len(self.edges) - 1):
                self.stack.append = (self.edges[j],r)
            while( len(self.stack)!= 0):
                pop=self.stack.pop()
                if self.visited.get(pop[0]) != True:
                    self.visited[pop[0]] = True
                    self.path[pop[0]] = pop[1]
                    self.edges = graph.getEdges(pop)
                    for j in range(len(self.edges) - 1):
                        self.stack.append = (self.edges[j], pop)
            return self.path

    def wholePath(n,m, path):
        temp=[]
        if n==m:
            return(n)
        else:
            while(path.get(m)!=n):
                m=path.get(m)
                temp.append(path.get(m))
            return(temp)
