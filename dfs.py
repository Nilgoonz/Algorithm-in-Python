
import graph

class dfs:

    def __init__(self,graph,r):
        nodes=graph.getNode()
        visited={}
        path={}
        for i in nodes :
            visited[i]=False
        for i in nodes :
            path[i]= ""

        stack=[]
        edges=graph.getEdge(r)
        path[r]=0
        visited[r]=True
        for j in range(len(edges) - 1):
            stack.append = ({edges[j],r})
        while( len(stack)!=0):
            pop=stack.pop()
            if visited.get(pop[0]) != True:
                visited[pop[0]]=True
                path[pop[0]]=pop[1]
                edges = graph.getEdge(pop)
                for j in range(len(edges) - 1):
                    stack.append = (edges[j], pop)
        return path

    def wholePath(n,m, path):
        temp=[]
        if n==m:
            return(n)
        else:
            while(path.get(m)!=n):
                m=path.get(m)
                temp.append(path.get(m))
            return(temp)
