class SearchLoop:

    noLoops = False

    def __init__(self,L):

        self.L= L

        self.noLoops = self.__checkloop(self.L)

    def __checkloop(self,L1):

        if L1.head.nextNode ==None:
            return not self.noLoops

        Newhead1 = L1.head
        print Newhead1.value
        Newhead2 = L1.head

        while(Newhead1 is not None and Newhead2 is not None):

            Newhead1 = Newhead1.nextNode
            print Newhead1.value
            Newhead2 = Newhead2.nextNode.nextNode

            if Newhead1 == Newhead2:
                return False
        return True
