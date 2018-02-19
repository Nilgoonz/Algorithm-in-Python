

class QuickFind():

    def __init__(self,N):
        self.id = range(0,N)

    def find(self,n,m):
        return self.id[n]==self.id[m]

    def union(self,n,m):
        p_id = self.id[n]
        for i in range(len(self.id)):
            if self.id[i] ==p_id:
                self.id[i]=self.id[m]
