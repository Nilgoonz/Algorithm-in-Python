class DutchFlag:

    def __init__(self,L):

        lenList = len(L)

        self.high = lenList-1;
        self.low = 0
        self.mid = 0
        self.L = L
        self.__check(self.L,self.high,self.low,self.mid)
    def __check(self,L,high,low,mid):

        i=0
        lenList = len(L)
        while high>mid :
            if L[mid] == 0:
                self.__swaap(L,low,mid)
                low = low+1
                mid = mid+1
            if L[mid] == 1:
                mid = mid +1
            if L[mid] == 2:
                self.__swaap(L,high,mid)
                high = high-1
            print L

            lenList = lenList-1


    def __swaap(self,L,a,b):

        temp = L[a]
        L[a] = L[b]
        L[b] = temp