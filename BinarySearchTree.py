
import Node
class BinarySearchTree:

    def __init__(self,root):
        self.key = root.key
        self.value=root.value


    def get(self,key,Root):

        while(Root!= None):
            if Root.key< key:
                NewRoot = Root.right
            if Root.key> key:
                NewRoot = Root.left
            if Root.key ==key:
                return Root.value
            Root = NewRoot
        return None

    def put(self,Node,Root):

        if Root==None:
            return Node
        if Root.key<Node.key:
            Root.right = self.put(Node,Root.right)
        elif Root.key>Node.key:
            Root.left=self.put(Node,Root.left)
        elif Root.key==Node.key:
            Root.value = Node.value
        return Root












