# write dfs without recursion
# import graph
from multiprocessing import Queue


class dfs:
    def __init__(self, graph, r):
        self.node = graph.getNode()
        self.visited = {}
        self.path = {}
        for i in self.node:
            self.visited[i] = False
        self.stack = []
        self.stack.append((r, r))
        self.path[r] = 0
        self.oldPath = 0
        self.__run__(graph)


    def __run__(self, graph):
        while len(self.stack):
            pop = self.stack.pop(0)
            print pop
            if not self.visited.get(pop[0]):
                self.path[pop[0]] = pop[1]
                self.visited[pop[0]] = True
                nodeList = graph.getEdge(pop[0])
                print self.stack
                for j in nodeList:
                    if not self.visited[j]:
                        self.stack.insert(0, (j, pop[0]))

